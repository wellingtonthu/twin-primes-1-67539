"""Standalone integer certificate. No floats enter any bound."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import factorial, isqrt
from functools import lru_cache
from heapq import heappush, heappop
from time import perf_counter_ns

Q = 1 << 80
n = 4096
H = 96000 * 60 * (1 << 12)
T = lam = F(5, 8)
rho = F(1, 5)


def up(a, b):
    return -(-a // b)


def scale(x):
    z = x * Q
    return up(z.numerator, z.denominator)


def logarithm(x, terms=48):
    assert x >= 1
    power = 0
    while x > 2:
        x /= 2
        power += 1

    def raw(z):
        v = (z - 1) / (z + 1)
        lo = 2 * sum(v**(2*j+1) / (2*j+1) for j in range(terms))
        return lo, lo + 2 * v**(2*terms+1) / ((2*terms+1)*(1-v*v))

    l, r = raw(x)
    if power:
        a, b = raw(F(2))
        l, r = l + power*a, r + power*b
    return l, r


def sieve_table():
    # Numerators sF(s), sf(s), with F,f divided by 2 exp(gamma).
    al, ah, bl, bh = ([0] * (12*n+1) for _ in range(4))
    al[n:3*n+1] = ah[n:3*n+1] = [Q] * (2*n+1)
    for k in range(2*n, 12*n):
        j = k-n
        # Integrated affine chord weights: alternate terms through k=4,5.
        wl = wr = Wl = Wr = 0
        p = j
        for m in range(1, 6):
            r, s = (m+1)*p, m*(m+1)*p
            if m < 5:
                wl += Q//s if m % 2 else -up(Q,s)
                wr += Q//r if m % 2 else -up(Q,r)
            Wl += up(Q,s) if m % 2 else -(Q//s)
            Wr += up(Q,r) if m % 2 else -(Q//r)
            p *= j
        assert 0 < wl <= Wl and 0 < wr <= Wr
        # On the preceding cell the numerator has |V''| <= 1.
        # s*F is convex (j >= 3n): chord >= true >= chord - e.
        # s*f is concave (j >= 2n): chord <= true <= chord + e.
        e = up(Q, 12*n*n*j)
        bl[k+1] = bl[k] + (wl*al[j]+wr*al[j+1])//Q - (e if j >= 3*n else 0)
        bh[k+1] = bh[k] + up(Wl*ah[j]+Wr*ah[j+1],Q)
        if k >= 3*n:
            al[k+1] = al[k] + (wl*bl[j]+wr*bl[j+1])//Q
            ah[k+1] = ah[k] + up(Wl*bh[j]+Wr*bh[j+1],Q) + e
    return ((al,ah),(bl,bh))


def reference_check():
    """Independent quarter-interval Taylor integration, outward at Q."""
    a, b = [([Q], 0)]*12, [([0], 0)]*8
    order = 44

    def step(last, delayed, j):
        p, ep = delayed
        end, e0 = last
        powers = [(-1)**m*j**(order-1-m) for m in range(order)]
        denom = j**order
        c = [sum(end)]
        for i in range(len(p)+order-1):
            x = sum(p[i-m]*powers[m] for m in
                    range(max(0,i-len(p)+1),min(i+1,order)))
            c.append(x//((i+1)*denom))
        err = (e0 + up(ep,j) + up(sum(map(abs,p)),j*denom)
               + len(c)-1)
        return c, err

    for k in range(8,48):
        b.append(step(b[-1],a[k-4],k-4))
        if k >= 12:
            a.append(step(a[-1],b[k-4],k-4))
    for s in range(4,13):
        for kind, seq in enumerate((a,b)):
            p, e = seq[4*s-1]
            x = sum(p)
            assert e*10**12 < Q
            assert TAB[kind][0][s*n] <= x-e <= x+e <= TAB[kind][1][s*n]
    print("Independent Taylor check: s=4,...,12 (both branches)",flush=True)


def at(kind, a, b):
    # Enclose F or f at a/b. For F alone 1/s extends below 1.
    assert b > 0
    if kind == 0 and a <= 3*b:
        assert a > 0
        return Q*b//a, up(Q*b,a)
    if kind == 1 and a <= 2*b:
        return 0, 0
    j, r = divmod(n*a,b)
    if j >= 12*n:
        return TAB[1][0][-1]//12, up(TAB[0][1][-1],12)
    lo, hi = TAB[kind]
    l = ((b-r)*lo[j]+r*lo[j+1])//a
    u = up((b-r)*hi[j]+r*hi[j+1],a)
    if r:
        e = up(Q*r*(b-r), 2*n*n*a*b)
        if kind == 0:
            l -= e
        else:
            u += e
    return l, u


@lru_cache(maxsize=None)
def slope(kind, i):
    """Magnitude of right derivative, rounded up at i/256 (where active)."""
    if kind == 1:
        i = max(512,i)
        return max(0, up(256*(at(0,i-256,256)[1]-at(1,i,256)[0]),i))
    if i <= 768:
        return up(Q*256**2,i*i)
    return max(0, up(256*(at(0,i,256)[1]-at(1,i-256,256)[0]),i))


def derivatives(kind, a, b, curvature):
    i = min(3072,256*a//b)
    assert i > 0
    d = slope(kind,i)
    if not curvature:
        return d, 0
    if kind == 0:
        p = slope(1,i-256) if i >= 768 else (Q//2 if a < 3*b else 0)
    else:
        i = max(i,512)
        p = slope(0,i-256)
    return d, up(256*(p+2*d), i)


def hcoord(a):
    z = a*H
    assert z.denominator == 1
    return z.numerator


def cap_const(a):
    return hcoord(a)*8


def line(c, coeff):
    return (cap_const(c), tuple(coeff))


def tent(d, ids):
    return (line(F(1,2),[4 if j in ids else 0 for j in range(d)]),
            line(F(1),[-12 if j in ids else 0 for j in range(d)]))


def value(p,c):
    return p[0]+sum(a*x for a,x in zip(p[1],c))


def plus(p,q,k=1):
    return (p[0]+k*q[0],tuple(a+k*b for a,b in zip(p[1],q[1])))


def complement(d, ids, upto):
    return tuple((0,tuple(8*((i in ids) or i<j)+16*(i==j)
                          for i in range(d)))
                 for j in range(upto) if j not in ids)


def parent(d):
    sets = ((0,),(0,1),(0,2),(1,2),(0,1,2))
    guards = ((),(),complement(d,sets[2],2),complement(d,sets[3],2),())
    w = (line(lam,[0,0,-3]+[0]*(d-3)),
         line(F(1),[0,-16,0]+[0]*(d-3)))
    return tuple((tent(d,I),g) for I,g in zip(sets,guards))+((w,()),)


def possible(forms, lo, hi):
    return [ts for ts, tests in forms
            if all(mx(plus(p,g,-1),lo,hi)>0 for p in ts for g in tests)]


def guaranteed(forms, lo, hi):
    return [ts for ts, tests in forms
            if all(mn(plus(p,g,-1),lo,hi)>0 for p in ts for g in tests)]


def all_models(c,lo,hi,forms):
    """A minorant of J and a list whose maximum majorizes J."""
    lower, upper = [], []
    for ps in possible(forms,lo,hi):
        a = min(ps,key=lambda p:value(p,c))
        upper.append(a)
    for ps in guaranteed(forms,lo,hi):
        a = min(ps,key=lambda p:value(p,c))
        if len(ps)==2:
            b = ps[1] if a==ps[0] else ps[0]
            e = max(0, mx(plus(a,b,-1),lo,hi))
            a = (a[0]-e,a[1])
        lower.append(a)
    return max(lower,key=lambda p:value(p,c)), upper


def mn(p,lo,hi):
    return p[0]+sum(a*(l if a>=0 else u) for a,l,u in zip(p[1],lo,hi))


def mx(p,lo,hi):
    return p[0]+sum(a*(u if a>=0 else l) for a,l,u in zip(p[1],lo,hi))


def subsets4():
    for ids in [(0,3),(1,3),(2,3),(1,2,3),(0,2,3),(0,1,3),(0,1,2,3)]:
        yield tent(4,ids), complement(4,ids,4)


P3, P4 = parent(3), parent(4)
C3 = line(F(0),[8,8,24,0])
ROOT = line(T,[0,0,0])
M4 = tuple(subsets4())
FAC = tuple(factorial(i) for i in range(5))


def cell(lo,hi):
    """Centroid, runs of identical intervals, and volume denominator."""
    d = len(lo)
    c = [0]*d
    runs = []
    factor = 1
    i = 0
    while i<d:
        j=i+1
        while j<d and (lo[j],hi[j])==(lo[i],hi[i]):
            j+=1
        m=j-i
        w=hi[i]-lo[i]
        assert w%(m+1)==0
        for k in range(i,j):
            c[k]=lo[i]+(j-k)*(w//(m+1))
        factor*=FAC[m]
        runs.append((i,j))
        i=j
    return c,runs,factor


def sigmag(coeff,v,c,lo,hi,runs):
    """Upper sd of (cap-S)/(8) - (v/(8c_last))*last, in H units.

    The coincidence simplex is an order-statistic law. Cauchy within
    a run and independence between runs bound 12 times the variance.
    """
    k=c[-1]
    ss=0
    for i,j in runs:
        a=0
        for l in range(i,j):
            w=hi[l]-lo[l]
            b=(coeff[l]-8)*k-(v if l==len(c)-1 else 0)
            a+=abs(b)*w
        ss+=a*a
    # sqrt(12) > 17/5.
    return up(5*(isqrt(ss)+1), 17*8*k)


def rinfo(p,c,lo,hi):
    """Central residual argument and certified lower and upper bounds."""
    co=tuple(a-8 for a in p[1])
    v=value(p,c)-8*sum(c)
    # Bound the first d-1 positions separately; ratio is monotone in last.
    r=(p[0],co[:-1]+(0,))
    l, u=mn(r,lo,hi),mx(r,lo,hi)
    ll,uu=(hi[-1] if l>=0 else lo[-1]),(lo[-1] if u>=0 else hi[-1])
    return v,l+co[-1]*ll,8*ll,u+co[-1]*uu,8*uu


def hinge(p,c,lo,hi,runs):
    """Upper mean of the positive part of an affine function."""
    if mx(p,lo,hi)<=0:
        return 0
    t=value(p,c)
    ss=0
    for i,j in runs:
        v=sum(abs(p[1][k])*(hi[k]-lo[k]) for k in range(i,j))
        ss+=v*v
    return up(isqrt(t*t+up(25*ss,289))+1+t,2)


def penalty(kind,reserve,ps,lo,hi,c,runs):
    a,b=rinfo(reserve,c,lo,hi)[1:3]
    if kind==0 and 256*a<b:
        return None
    w=sum(hinge(p,c,lo,hi,runs) for p in ps)
    if not w:
        return 0
    return up(derivatives(kind,max(a,2*b) if kind==1 else a,b,False)[0]*w,8*lo[-1])


def at_slope(kind,a,b,l,u):
    """Bounds for the nonnegative slope magnitude at a center."""
    if kind==1 and a<=2*b:
        return 0,0
    if kind==0 and a<=3*b:
        return Q*b*b//(a*a),up(Q*b*b,a*a)
    x,y=at(1-kind,a-b,b)
    v,w=(x-u,y-l) if kind==1 else (l-y,u-x)
    return max(0,v*b//a), max(0,up(w*b,a))


def integrated(kind,p,alt,lo,hi,c,runs,fac,extra):
    """Upper (kind=1) or lower (kind=0) integral of phi(p)-phi(alt).

    Returns the directed endpoint and a central estimate used solely
    to select the subdivision order.
    """
    d=len(c)
    w=1
    dl=lo[-1]
    pc=pl=1
    aW=aV=bW=0
    for i,(t,l,u) in enumerate(zip(c,lo,hi)):
        a=1+(i==d-1)
        wid=u-l
        w*=wid
        pc*=t**a
        pl*=l**a
        q=up(Q*5*wid,17*l)
        aW+=a*q
        aV+=(a+(i==d-1))*q
        bW+=a*q*q
    # vol*W at centroid and its maximum, including scale conversion.
    if kind==1:
        wc=up(2*H*w*Q,fac*pc)
    else:
        wc=2*H*w*Q//(fac*pc)
    wl=up(2*H*w*Q,fac*pl)
    vc,la,lb,ra,rb=rinfo(p,c,lo,hi)
    vd,ma,mb,sa,sb=rinfo(alt,c,lo,hi)
    den=8*c[-1]
    if kind==1 and ra<=2*rb:
        return 0,0
    if kind==0 and (256*la<lb or 256*ma<mb):
        return 0,0
    vl,vh=at(kind,vc,den)
    ul,uh=at(kind,vd,den)
    x = max(0,(vh-ul) if kind==1 else (vl-uh))
    if kind==0 and x==0:
        return 0,0
    E = extra
    sd=[0,0]
    for isalt,(f,g,a,b,r,s) in enumerate(((p,vc,la,lb,ra,rb),(alt,vd,ma,mb,sa,sb))):
        if kind==1 and (r<=2*s or (isalt and g<=2*den)):
            continue
        sigma=sigmag(f[1],g,c,lo,hi,runs)
        q=up(Q*sigma,dl)
        sd[isalt]=q
        _,C=derivatives(kind,max(a,2*b) if kind==1 else a,b,isalt)
        if C:
            E+=up(C*q*q,2*Q*Q)
        if kind==1 and not isalt and a<2*b:
            E+=up(q,4)
    a,b=at_slope(kind,vc,den,vl,vh)
    i,j=at_slope(kind,vd,den,ul,uh)
    P=b*sd[0]+j*sd[1]
    if sd[0] and sd[1] and b and j:
        coeff=tuple(8+s-t for s,t in zip(p[1],alt[1]))
        q=up(Q*sigmag(coeff,vc-vd,c,lo,hi,runs),dl)
        e=max(b-i,j-a)
        P=min(P,b*q+e*sd[1],j*q+e*sd[0])
    E+=up(P*aV,Q*Q)
    if kind==1:
        E+=up(x*(aW*aW+bW),2*Q*Q)
        z=up(wc*x+wl*E,Q)
    else:
        z=max(0,(wc*x-wl*E)//Q)
    return z,wc*x//Q


def estimate(lo,hi,d):
    c,runs,fac=cell(lo,hi)
    if d==3:
        if mx((cap_const(T),(-8,-8,-24)),lo,hi)<=0:
            return 0,0,False
        ps=max(guaranteed(P3,lo,hi),key=lambda k:min(value(p,c) for p in k))
        p=min(ps,key=lambda p:value(p,c))
        extra=0
        if len(ps)==2:
            b=ps[1] if p==ps[0] else ps[0]
            err=plus(p,b,-1)
            shift=max(0,mx(err,lo,hi))
            if shift:
                extra=penalty(1,(p[0]-shift,p[1]),(err,),lo,hi,c,runs)
        u,m=integrated(1,ROOT,p,lo,hi,c,runs,fac,extra)
        return u,max(0,u-m),False
    low, ps=all_models(c,lo,hi,P4)
    if all(mx(plus(p,C3,-1),lo,hi)<=0 for p in ps):
        return 0,0,False
    old=max(ps,key=lambda p:value(p,c))
    center=value(old,c)
    good=mn(plus(low,C3,-1),lo,hi)>0
    extra=penalty(0,old,(plus(b,old,-1) for b in ps if b!=old),lo,hi,c,runs) if good else None
    lu, guess=0,0
    V=1
    P=c[-1]
    for l,h,j in zip(lo,hi,c):
        V*=h-l
        P*=j
    for ts, tests in M4:
        # A certificate box uses just the selected branch yielding its
        # greatest bound. It is legal to leave the cap unchanged when
        # the candidate fails to improve it.
        m=min(ts,key=lambda p:value(p,c))
        a=value(m,c)
        if any(mx(plus(m,p,-1),lo,hi)<=0 for p in (low,*tests)):
            continue
        r=max(a,center)
        s=8*sum(c)
        oldcen=max(center, s+8*c[-1])
        e=at(0,oldcen-s,8*c[-1])[1]-at(0,max(r,oldcen)-s,8*c[-1])[0]
        guess=max(guess, V*2*H*max(0,e)//(fac*P))
        if extra is None:
            continue
        other=ts[1] if m==ts[0] else ts[0]
        if all(mn(plus(k,p,-1),lo,hi)>0 for p in tests for k in ts):
            if a>center:
                error=plus(m,other,-1)
                shift=max(0,mx(error,lo,hi))
                cost=penalty(0,(m[0]-shift,m[1]),(error,),lo,hi,c,runs) if shift else 0
                if cost is None:
                    continue
                g,_=integrated(0,old,m,lo,hi,c,runs,fac,extra+cost)
                lu=max(lu,g)
    return lu,max(0,guess-lu),not good


def children(lo,hi,d,boundary):
    _,runs,_=cell(lo,hi)
    weights=(2,2,5) if d==3 else ((2,2,5,0) if boundary else (2,2,3,5))
    eligible=[(max(weights[i:j])*(hi[i]-lo[i]),i,j) for i,j in runs
              if (hi[i]-lo[i])%120==0 and (hi[i]-lo[i])>=240]
    if not eligible:
        return
    _,i,j=max(eligible)
    for k in range(j-i+1):
        l,h=list(lo),list(hi)
        for a in range(i,j):
            m=(lo[a]+hi[a])//2
            if a<i+k:
                l[a]=m
            else:
                h[a]=m
        yield tuple(l),tuple(h)


def integral(d,delta,goal,initial,limit):
    lower=hcoord(delta)
    upper=hcoord(rho)
    assert (upper-lower)%initial==0
    dh=(upper-lower)//initial
    heap=[]
    total=calls=0

    def push(l,h):
        nonlocal total,calls
        x,e,boundary=estimate(l,h,d)
        calls+=1
        total+=x
        if e and any((b-a)%120==0 and b-a>=240 for a,b in zip(l,h)):
            heappush(heap,(-e,calls,l,h,x,boundary))

    for row in combinations_with_replacement(range(initial),d):
        l=tuple(lower+i*dh for i in row[::-1])
        push(l,tuple(t+dh for t in l))
    target=scale(goal)
    while heap and calls<limit and ((total>target) if d==3 else (total<target)):
        _,_,l,h,x,boundary=heappop(heap)
        total-=x
        for a,b in children(l,h,d,boundary):
            push(a,b)
    print(f"rank {d}: {calls} box/simplex evaluations; {total}/{Q}",flush=True)
    return F(total,Q)


def main():
    global TAB
    start=perf_counter_ns()
    assert 0 < F(19,1000) < F(30,1000) < rho == F(1,5)
    assert 3*rho < T == lam == F(5,8) and 3 < T/rho < 4
    assert (F(1)-3*rho)/2 == rho
    TAB=sieve_table()
    reference_check()
    delta=F(19,1000)
    assert (rho-delta)/delta > 9
    # D decreases and D(s)<=D(9)*(9/s)^2.
    d9=F(at(0,9,1)[1]-at(1,9,1)[0],Q)
    assert 0 < d9 < F(1,10**6)
    _, lr=logarithm(rho/delta)
    tail=F(scale(81*d9*delta*(lr*lr+2*lr+2)/(rho-delta)**2),Q)
    ref=T/rho
    i1=F(scale(F(2,rho)*F(at(0,ref.numerator,ref.denominator)[1],Q)-2/T),Q)
    core=integral(3,delta,F(55,1000),32,435000)
    save=integral(4,F(30,1000),F(185,10000),20,700000)
    assert 0 < i1 < (T/rho-3)**2/(2*T)
    assert 0 < tail < F(1,10000) and 0 < core < F(56,1000)
    assert save >= F(16,1000)
    # Independent approximation allowances (finite policy and attachment).
    u=F(1,1000000)
    base=F(scale(2/T+i1+tail+core+2*u),Q)
    K=base-save
    assert base <= F(32669,10000)
    assert K <= F(32509,10000)
    print(f"I1 <= {scale(i1)}/{Q}; I3,c <= {scale(core)}/{Q}; I3,t <= {scale(tail)}/{Q}")
    print(f"U0+2u <= {scale(base)}/{Q}; G1 >= {scale(save)}/{Q}; K <= {scale(K)}/{Q}")
    c=F(12759,10000)
    b=F(3539,5000)
    _, loghi=logarithm(1/b)
    shortcut=c-2*(1-b+loghi)
    assert F(2,5) < b/(1+b) < F(1,2)
    print(f"Shortcut b={b}; margin >= {shortcut.numerator*Q//shortcut.denominator}/{Q}")
    assert shortcut.numerator*Q//shortcut.denominator > 0
    for b,k in [(F(6767,10000),base),(F(17,25),K),(F(169,250),K),
                (F(3377,5000),K),(F(67539,100000),K)]:
        m=c-k*logarithm(1/b)[1]
        ml=m.numerator*Q//m.denominator
        print(f"c={c}; b={b}; K_num={scale(k)}; margin >= {ml}/{Q}")
        assert ml > 0
    elapsed=perf_counter_ns()-start
    print(f"Elapsed: {elapsed//10**9}.{elapsed//10**6%1000:03d} s")


if __name__ == '__main__':
    main()
