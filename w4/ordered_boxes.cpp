#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>
using I = int64_t;
using W = __int128_t;
using Point = std::array<I,4>;
constexpr I H=100*(1<<20), n=4096, rate=1000000000000LL;
constexpr W unit=W(rate)*rate;
constexpr I tiny=-2000000000LL, huge=-tiny;
struct Form { I a; Point k; };
struct Box { Point lo,hi; };
Form operator-(Form f,Form g) {
    f.a-=g.a;
    for (int i=0;i<4;++i) f.k[i]-=g.k[i];
    return f;
}
I ext(const Form& f,const Box& b,bool upper) {
    I a=f.a;
    for(int i=0;i<4;++i) a+=f.k[i]*((f.k[i]>=0)==upper ? b.hi[i] : b.lo[i]);
    return a;
}
struct Branch {
    std::array<Form,2> planes;
    std::vector<Form> tests;
};
Branch tent(int mask,int guard_mask=0) {
    Form p{4*H,{}},q{8*H,{}};
    for(int i=0;i<4;++i) if(mask>>i&1) {p.k[i]=4;q.k[i]=-12;}
    Branch result{{p,q},{}};
    for(int i=0;i<4;++i) if(guard_mask>>i&1){
        Form g{0,{}};
        for(int j=0;j<4;++j) if((mask>>j&1)||j<i) g.k[j]=8;
        g.k[i]=16;
        result.tests.push_back(p-g);
        result.tests.push_back(q-g);
    }
    return result;
}
const Form cube{0,{8,8,24,0}};
const Form whole{0,{8,8,8,8}};
const Form bp{8*H,{0,-16,0,0}};
const std::array<Form,2> w4{Form{5*H,{0,0,0,-3}},bp};
const std::array<Branch,6> parents={
    tent(1),tent(3),tent(5,2),tent(6,1),tent(7),
    Branch{{Form{5*H,{0,0,-3,0}},bp},{}}
};
const std::array<Branch,7> fourth={
    tent(9,6),tent(10,5),tent(12,3),tent(11,4),tent(13,2),tent(14,1),tent(15)
};
I floorq(I a,I b) { return a>=0 ? a/b : -((-a+b-1)/b); }
I roundarg(const Form& f,const Box& b,bool upper) {
    Form r=f-whole;
    I k=r.k[3];
    r.k[3]=0;
    I a=ext(r,b,upper);
    I t=((a>=0)==upper) ? b.lo[3] : b.hi[3];
    I num=n*(a+k*t), den=8*t;
    return upper ? -floorq(-num,den) : floorq(num,den);
}
struct Sieve {
    std::array<I,13*n> lo,hi,slo,shi;
    I get(I j,bool upper) const {
        j=std::max(n,std::min(12*n,j));
        return upper?hi[j]:lo[j];
    }
    I slope(I j,bool upper) const {
        if(!upper&&j>12*n) return 0;
        j=std::max(n,std::min(12*n,j));
        return upper?shi[j]:slo[j];
    }
} sieve;
struct Interval { W lo,hi; };
Interval assess(const Box& b) {
    I oldL=n,oldU=n,wL=huge,wU=huge,dL=huge,dU=huge;
    bool full=false,possible=false;
    for(Form w:w4) {
        wL=std::min(wL,roundarg(w,b,false));
        wU=std::min(wU,roundarg(w,b,true));
    }
    if(wU<=n)return {0,0};
    auto scan=[&](const Branch& br,bool parent){
        bool guaranteed=true;
        for(Form f:br.tests){
            if(ext(f,b,true)<=0)return;
            if(ext(f,b,false)<=0)guaranteed=false;
        }
        bool cubePossible=true,cubeFull=true;
        I lower=huge,upper=huge,dHigh=tiny;
        std::array<I,2> dLow{tiny,tiny};
        for(Form p:br.planes){
            if(parent){
                cubePossible&=ext(p-cube,b,true)>0;
                cubeFull&=ext(p-cube,b,false)>0;
            }
            I pHigh=huge;
            for(int j=0;j<2;++j){
                Form difference=w4[j]-p;
                if(guaranteed)pHigh=std::min(pHigh,ext(difference,b,true));
                dLow[j]=std::max(dLow[j],ext(difference,b,false));
            }
            dHigh=std::max(dHigh,pHigh);
            lower=std::min(lower,roundarg(p,b,false));
            upper=std::min(upper,roundarg(p,b,true));
        }
        if(parent){
            possible|=cubePossible;
            full|=guaranteed&&cubeFull;
        }
        dL=std::min(dL,std::min(dLow[0],dLow[1]));
        oldU=std::max(oldU,upper);
        if(guaranteed){
            oldL=std::max(oldL,lower);
            dU=std::min(dU,dHigh);
        }
    };
    for(const Branch& br:parents)scan(br,true);
    if(!possible||dU<=0||wU<=oldL)return {0,0};
    for(const Branch& br:fourth)scan(br,false);
    if(dU<=0||wU<=oldL)return {0,0};
    I fl=0;
    if(full){
        if(wL>oldU)fl=std::max<I>(0,sieve.get(oldU,false)-sieve.get(wL,true));
        if(dL>0)fl=std::max<I>(fl,W(dL)*sieve.slope(wU,false)/(8*b.hi[3]));
    }
    I fu=std::max<I>(0,sieve.get(oldL,true)-sieve.get(wU,false));
    fu=std::min<I>(fu,(W(dU)*sieve.slope(oldL,true)+8*b.lo[3]-1)/(8*b.lo[3]));
    assert(fl<=fu);
    if(fu==0)return {0,0};
    I fact=1,run=1;
    W weightLo=unit,weightHi=unit;
    for(int j=0;j<4;++j){
        I wid=b.hi[j]-b.lo[j];
        if(j>0&&b.lo[j]==b.lo[j-1]&&b.hi[j]==b.hi[j-1])fact*=++run;
        else run=1;
        weightLo=weightLo*wid/b.hi[j];
        weightHi=(weightHi*wid+b.lo[j]-1)/b.lo[j];
    }
    I dl=fact*b.hi[3],du=fact*b.lo[3];
    weightLo=weightLo*(2*H)/dl;
    weightHi=(weightHi*(2*H)+du-1)/du;
    return {weightLo*fl/rate,(weightHi*fu+rate-1)/rate};
}
struct Task{Box b;Interval z;};
struct Priority{
    bool operator()(const Task& a,const Task& b)const{
        W gapA=a.z.hi-a.z.lo,gapB=b.z.hi-b.z.lo;
        if(gapA!=gapB)return gapA<gapB;
        if(a.b.lo!=b.b.lo)return a.b.lo<b.b.lo;
        return a.b.hi<b.b.hi;
    }
};
std::string str(W x) {
    if(x==0)return "0";
    std::string s;
    for(;x;x/=10)s.push_back(char('0'+x%10));
    std::reverse(s.begin(),s.end());
    return s;
}
std::vector<Box> split(const Box& b) {
    const Point weights{2,2,3,5};
    int start=-1,end=-1;
    I best=0;
    for(int i=0,j;i<4;i=j){
        j=i+1;
        while(j<4&&b.lo[j]==b.lo[i]&&b.hi[j]==b.hi[i])++j;
        I width=b.hi[i]-b.lo[i],score=weights[j-1]*width;
        if(width%2==0&&score>best){best=score;start=i;end=j;}
    }
    if(start<0)return {};
    I mid=(b.lo[start]+b.hi[start])/2;
    std::vector<Box> result;
    for(int k=start;k<=end;++k){
        Box a=b;
        for(int j=start;j<end;++j)if(j<k)a.lo[j]=mid;else a.hi[j]=mid;
        result.push_back(a);
    }
    return result;
}
int main(int argc,char** argv) {
    std::ifstream in("sieve_table.txt");
    for(I i=n;i<=12*n;++i){
        in>>sieve.lo[i]>>sieve.hi[i]>>sieve.slo[i]>>sieve.shi[i];
        assert(in&&sieve.lo[i]<=sieve.hi[i]&&sieve.slo[i]<=sieve.shi[i]);
    }
    std::priority_queue<Task,std::vector<Task>,Priority> queue;
    W sumLo=0,sumHi=0;
    I evaluated=0,limit=argc>1?std::stoll(argv[1]):3000000;
    auto push=[&](const Box& b){
        Interval z=assess(b);
        sumLo+=z.lo;sumHi+=z.hi;++evaluated;
        if(z.hi>z.lo)queue.push({b,z});
    };
    constexpr I bins=16,start=3*H/100,step=(H/5-start)/bins;
    static_assert(start+bins*step==H/5);
    for(int i=0;i<bins;++i)for(int j=0;j<=i;++j)for(int k=0;k<=j;++k)for(int l=0;l<=k;++l){
        Point lo{start+i*step,start+j*step,start+k*step,start+l*step},hi=lo;
        for(I& x:hi)x+=step;
        push({lo,hi});
    }
    I logAt=100000;
    while(!queue.empty()&&evaluated<limit){
        auto task=queue.top();
        queue.pop();
        auto children=split(task.b);
        if(children.empty())continue;
        sumLo-=task.z.lo;sumHi-=task.z.hi;
        for(const auto &b:children)push(b);
        if(evaluated>=logAt){
            std::cout<<evaluated<<" "<<str(sumLo)<<" "<<str(sumHi)<<" / "<<str(unit)<<std::endl;
            logAt*=2;
        }
    }
    std::cout<<evaluated<<" "<<str(sumLo)<<" "<<str(sumHi)<<" / "<<str(unit)<<std::endl;
}
