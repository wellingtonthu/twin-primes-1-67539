# A positive upper sieve for balanced semiprimes at distance two

Let \(C_2=2\prod_{\ell>2}(1-(\ell-1)^{-2})\) and \(H(x)=C_2x/(\log x)^2\). For \(0<b<1\), let \(A_b(x)\) count primes \(p\le x\) for which \(p+2=rq\) with \(q\) prime, \(r=1\) or prime, and \(r\le q^b\).

**Theorem.** Proposition \((1-1.67539)\) is true unconditionally. More precisely, at \(b=67539/100000\),
\[
\liminf_{x\to\infty} A_b(x)/H(x)
\ \ge\ \frac{56380964408304863785}{1208925819614629174706176}
\ >\ 0.0000466 .
\]
In particular \(A_b(x)>0.0000466 H(x)\) for every sufficiently large \(x\). The rank-three construction alone gives Proposition \((1-1.6767)\). Both improve Li–Liu's unconditional Proposition \((1-1.75)\), arXiv:2606.05224v2, Theorem 1.2.

The external inputs for the theorem are Runbo Li's published Chen count (*Mathematical Reports* **28** (2026), 39–61, Theorem 1.3, arXiv:2405.05727v4), Pascadi's fixed nonzero residue convolution estimate (arXiv:2505.00653v1, Proposition 4.4), the classical prime number theorem, Mertens, prime and Möbius Siegel–Walfisz, the multiplicative large sieve and the complete Weil bound for Kloosterman sums, and the standard dimension-one linear Rosser sieve and fundamental lemma (Iwaniec, *Acta Arith.* **36** (1980), 171–202; Friedlander–Iwaniec, *Opera de Cribro*). All distribution deductions for the new weights and the interval calculation are given below.

We adapt [Chan's Goldbach argument](https://aixiv.science/pdf/aixiv.261111.000001v1.0.pdf), in particular the positive prefix sieve, the rank-three and rank-four cap changes (Appendix F), and the subtraction of excluded semiprimes (§8). At the fixed residue 2, we use Pascadi's \(5/8\) estimate and verify the modified modulus factorizations and density bounds for the resulting sieve.

## 1. The subtraction and an elementary shortcut

Let \(B_b(x)\) count primes \(p\le x\) with \(p+2=rq\), \(r,q\) prime and \(q^b<r\le q\). Order the two factors; each semiprime then has exactly one factorization, including squares. Prime residuals all belong to \(A_b\). Allowing for at most one exception at \(p=2\), Li's theorem gives
\[
\liminf_{x\to\infty}A_b(x)/H(x)\ \ge\ 12759/10000-\limsup_{x\to\infty}B_b(x)/H(x).
\tag{1}
\]
In odd moduli the congruence for \(rq-2\) is \(rq\equiv2\); the two-prime sequence has local density \(g(\ell)=1/(\ell-1)\) for odd primes \(\ell\), with no factor at 2. Indeed \((1-g(\ell))/(1-1/\ell)=1-(\ell-1)^{-2}\). Thus, with \(P(y)=\prod_{2<\ell<y}\ell\) and \(V(y)=\prod_{2<\ell<y}(1-g(\ell))\),
\[
V(x^t)\sim\frac{e^{-\gamma}C_2}{t\log x}
\tag{2}
\]
uniformly on compact positive \(t\)-ranges. The 2 from omitting the even prime is already in \(C_2\). This agrees with Li–Liu (6.6)–(6.10), for which the Mertens multiplier in \(C_2\)-units is \(12e^{-\gamma}\) at \(x^{1/12}\), and with Pascadi's \(\Pi_2\) in Corollary 1.4.

**Two-factor shortcut.** Use Li–Liu's Lemma 3.4 (arXiv:2606.05224v2), the fixed-residue bilinear estimate for one-bounded well-factorable modulus weights of order 1. Take \(N\) to be the shorter dyadic scale (\(r\)); prime coefficients satisfy its Siegel–Walfisz and roughness conditions. In the bad region, \(\nu=\log N/\log X\) belongs to \([2/5,1/2]\) for large \(x\) if \(b>2/3\), allowing bounded dyadic endpoint errors and taking the smaller scale if needed. The table gives level \(X^{1-\nu-\epsilon}\). On each chart use Iwaniec's well-factorable upper linear sieve of order 1 (as stated in Li–Liu Lemma 2.5) with root at a third of the level exponent. For \(rq\asymp x\), \(t=\log r/\log x\), its density tends to \(2/(1-t)\) in \(C_2/\log x\) units when the fixed sieve tolerances are sent to zero after the asymptotic. The level and asymptotic are uniform on the compact range in question; equivalently one can use finitely many \(t\)-bins and in each the minimum allowed level. Smooth separation of pair weights as in §4 preserves prime Siegel–Walfisz by partial summation. The range \(rq<\sigma x\) contributes \(O(\sigma H(x))\) by using a fixed lower level and §6 after discarding logarithmically small products. Integrating against \(dt/[t(1-t)]\) gives
\[
\limsup_{x\to\infty}\frac{B_b(x)}{H(x)}
\ \le\ \int_{b/(1+b)}^{1/2}\frac{2\,dt}{t(1-t)^2}
\ =\ 2(1-b-\log b).
\]
The antiderivative divided by 2 is \(\log(t/(1-t))+(1-t)^{-1}\). In particular the margin \(1.2759-2(1-b-\log b)>0\) at \(b=3539/5000\), checked in §7, gives \(1-1.7078\).

## 2. The positive tree and its proposed caps

Write \(L=\log x\), \(\rho=1/5\), \(T=5/8\), \(v(u)=\min((1+u)/2,1-3u/2)\). Order the primes of a squarefree modulus decreasingly and write \(t_i=\log \ell_i/L\), \(S_j=\sum_{i\le j}t_i\). Start with root primes below \(x^{\rho'}\), where \(\rho'<\rho\) may be taken arbitrarily close to \(\rho\). A prefix at odd rank \(j\) passes if \(S_{j-1}+3t_j\) is strictly below its current cap. Every even child of an admitted prefix is kept. At rank one use \(T\); at rank three, before its cube test, switch to the cap \(J(t_1,t_2,t_3)\) defined below. Later inherit the cap, except for the optional rank-four increase. We start with ideal caps and then insert fixed reserves before applying the analytic estimates.

For \(t_1=u\ge t_2=v_2\ge t_3=w_3\) define \(J\) as the maximum of:

* \(v(t_1),v(t_1+t_2),v(t_1+t_2+t_3)\);
* \(v(t_1+t_3)\), if it exceeds \(t_1+t_3+2t_2\);
* \(v(t_2+t_3)\), if it exceeds \(t_2+t_3+2t_1\);
* \(\min(5/8-3t_3/8,1-2t_2)\).

The extra \(1-2t_2\) is required: \(2\rho=2/5>1-5/8\). No unguarded nonleading complementary square is used.

At an admitted rank-four prefix \(t\) with \(t_4\ge3/100\), test every subset \(I\) containing index 4 and at least one other index. Write \(u_I=\sum_{i\in I}t_i\). Raise the cap to the greatest \(M=v(u_I)>J\) over the candidates satisfying
\[
u_I+\sum_{i<j,\ i\notin I}t_i+2t_j<M\qquad(j\le4,\ j\notin I).
\tag{3}
\]
If none passes, retain \(J\). Rank four is even so this increase is made without a retention test there.

For any finite prime set and multiplicative \(0\le g(\ell)\le1\), the density of a prefix tree \(\mathcal T\) of this form satisfies
\[
\sum_{d\in\mathcal T}\mu(d)g(d)=
\prod_\ell(1-g(\ell))+
\sum_{e\text{ first omitted prefix}}g(e)\prod_{\ell<\ell_{\rm last}(e)}(1-g(\ell)).
\tag{4}
\]
Group the terms removed from full inclusion–exclusion by their unique first omitted prefix. It has odd rank, and all its formal continuations sum to the negative of the displayed term. In particular, taking \(g(\ell)={\bf1}_{\ell\mid n}\) proves that the tree sum is nonnegative and majorizes the coprimality indicator pointwise. Replacing the cap after rank four does not change the parity of any first exit.

## 3. Capacity verification and realization

Write \(S_{j-1}+2t_j\) for the full square at slot \(j\). For selected slots \(I\) the complementary squares are the expressions on the left of (3). After the last selected slot, each complementary square is the full square. A passing odd cube implies both its own square and the next square. The first two full squares are bounded by \(3t_1\), whereas \(v(t_1)=(1+t_1)/2>3t_1\) for \(t_1<1/5\). The third cube controls the third and fourth full squares even if the fourth cap is raised. For \(I=\{1\}\), complementary squares are full squares. For \(I=\{1,2\}\) the only complementary square up to rank three is a full square; for \(I=\{1,2,3\}\) there is none. For \(I=\{1,3\}\) and \(\{2,3\}\), the only extra square is exactly its corresponding test in §2. For rank four this is precisely (3).

Here is the factorization proof. Let \(X\) be the sequence scale (\(MN\asymp X\) in Pascadi), and let \(U\in[X^{2\zeta},X^{1/3+\zeta/2}]\) be the selected medium length. We convert exponents from base \(x\) to base \(X\); below this change is arbitrarily small. Fix a covering exponent \(\ell>1/2\) slightly above the cap and set \(D=X^{\ell-2\zeta}\), \(A=UX^{-\zeta}\). Fix a covering reserve \(\delta>4\zeta\) and require all full square exponents to be at most \(\ell-\delta\), together with the complementary square exponents when a subset is prescribed. Pascadi (4.15) requires, for the three modulus lengths,
\[
Q_1\le UX^{-\epsilon},\qquad U^2Q_2Q_3^2\le X^{1-15\epsilon},
\qquad U^2Q_2^5Q_3^2\le X^{2-40\epsilon}.
\tag{5}
\]
The coefficient on the \(U\) side must be one-bounded, Siegel–Walfisz in the sense of his Definition 4.3, and supported on integers with least prime factor at least \(X^{1/(\log\log X)^3}\). The other coefficients are one-bounded and the modulus coefficients supported on odd integers. The fixed residue is 2. There is no extra exceptional-spectrum restriction in (5).

If the selected product has upper endpoint \(B=X^\beta\), the covering inequalities \(\ell<v(\beta)\) mean
\[
b_-=2\ell-1<\beta<b_+=(2-2\ell)/3 .
\tag{6}
\]
If \(C=D/(AB)\ge1\), place the selected slots in group two and pack the rest greedily in \(A,C\). If a slot \(s\) fits neither, the product of the remaining capacities is less than \(s^2\), contradicting the complementary square. With endpoint capacities \((A,B,C)\), the two monomials in (5), using \(A\) for \(U\), are \(D^2/B,D^2B^3\), at most \(X^{1-4\zeta},X^{2-4\zeta}\) even at equality in (6). Replacing \(A\) by \(U\) uses \(2\zeta\), leaving fixed savings. If \(C<1\), repack all slots using their full squares into \(A,D/A\) (both at least 1 for small \(\zeta\)) and take group three empty. Here \(D/A<B\) and \(D/A\ge X^{\ell-1/3-3\zeta/2}>1\). After restoring \(U\), the last monomial is \(X^{2\zeta}D^2(D/A)^3<X^{2\zeta}D^2B^3\). The first is \(U^2(D/A)=X^{2\zeta}AD\le X^{1/3+\ell-\zeta/2}\le X^{23/24-\zeta/2}<X^{1-4\zeta}\) for the chosen small \(\zeta\). This is also the two-factor repair used by Pascadi, Lemma 5.6.

For the three-slot alternative require \((1+t_1)/2<\ell<5/8-3t_3/8\) and \(2t_2\le1-\ell-\delta\). Start with \(A,X^{b_-},D/(AX^{b_-})\). If the last capacity is below 1 use the same two-group repair. Otherwise place the largest slot in group two. The second slot fits group one or three because its square is at most \(X^{1-\ell-\delta}<X^{1-\ell-2\zeta}\), the product of their capacities. Continue greedily. At the first failure the slot \(s\) has exponent at most \(t_3\), and can be adjoined to group two with a new product endpoint \(B'\in[X^{b_-},X^{b_-+t_3}]\): indeed \(b_+-b_-=(5-8\ell)/3>t_3\). If the old products are \(a_1,a_2,a_3\), then \(A<a_1s\) and \(a_1a_2a_3s^2\le D\), so \(AB'a_3<D\) with \(B'=a_2s\) (failure in group two gives \(B'>X^{b_-}\)). Freeze \(B'\) and continue in groups one and three using the full squares. Without failure the original capacities work at \(\beta=b_-\). The same monomial bounds hold at the nonstrict endpoints \(b_-\le\beta\le b_+\), with the explicit \(2\zeta\) savings. This branch need only be used when it strictly exceeds the fallback \(v(t_1)\).

**Finite realization.** Fix \(a_*>0\), the density allowance \(u_0>0\), the root cutoff \(\rho'<\rho\), and the tail cutoff \(\delta_0>0\). Work first in base \(x\). Freeze the branch and physical cap \(\lambda_{\rm phys}\) on each of finitely many coarse cells. Where packing is used, choose a covering exponent \(\ell>\lambda_{\rm phys}\) below the relevant ideal endpoint.

- Small \(t_1\) uses a fixed ordinary cap below \(1/2\). Rough ranks at most two have total exponent at most \(2\rho<1/2\). Both gaps allow the absolute mean value bound.
- At the third-slot tail and trimmed walls, use \(I=\{1\}\) with a slightly lowered \(v(t_1)\). Outside the small-\(t_1\) range, \(v(t_1)>1/2\) uniformly, and \(v(t_1)-3t_1\ge(1-5\rho')/2>0\) makes room for the first two full squares below the physical cap. The actual third cube test is \(t_1^++t_2^++3t_3^+<\lambda_{\rm phys}\) on interval upper endpoints. It bounds full squares three and four. Later squares follow from odd cube tests, and for \(I=\{1\}\) the complementary squares are full squares.
- In compact third-rank cells, require a fixed gap in each extra complementary-square guard, if present, and lower the selected physical cap by less than these gaps. Trim near ties so that the physical cap still exceeds the fallback cap. The first two full squares are bounded using the fallback, and the remaining full squares follow from passing odd cubes. For \(W\), trim near ties with the fallback and choose \(\ell\) between \(\max\{\lambda_{\rm phys},(1+t_1)/2\}\) and \(\min\{5/8-3t_3/8,1-2t_2\}\) throughout each retained cell. This supplies a separate gap in \(2t_2<1-\ell\).
- In compact fourth-rank cells, trim near equality in (3) and in the improvement over the inherited cap, then lower the new cap by less than these gaps. The inherited third cube controls full squares three and four. Later odd cubes use the new cap. The additional complementary squares through slot four follow from (3) and agree with full squares after the last selected slot. Other cells inherit the parent rule.

On finitely many retained cells take a common \(\delta_1>0\) smaller than the gaps \(\ell-\lambda_{\rm phys}\), the analytic endpoint and guard gaps, and the absolute-mean-value gaps. The trimming and the fallback at small \(t_3\) cost arbitrarily little in density by §5. This preserves a positive gap above \(t_1+t_2\), since \(J-t_1-t_2\ge(1-3\rho)/2\) before lowering.

Set \(\delta=\delta_1/4\) and choose \(0<\zeta<\min(10^{-5},\delta/4,a_*/24)\), followed by \(\eta,\epsilon>0\) small enough for the packing and attachment. The rough tree on primes at least \(x^\eta\) has bounded rank. Refine its common alphabet so that using upper endpoints costs at most \(\delta_1/4\) in the initial inequalities. Test odd cubes on those endpoints at the physical cap and include even children automatically. Finally choose \(\kappa\) as in §4. On charts \(X\gg x^{1-\kappa}\), multiplying exponents by \(\log x/\log X=1+O(\kappa+L^{-1})\) costs at most another \(\delta_1/4\) in the inequalities. For the later full squares one can rescale the physical-cap bound directly. The reserve \(\delta\) therefore holds in base \(X\), including \(2t_2\le1-\ell-\delta\) in the \(W\) branch.

For a rough atom of sign \(+\) or \(-\), attach the corresponding ordinary upper or lower small-prime weights on \(\ell<x^\eta\), supported below \(x^{\sqrt\eta}\) and with absolute value at most one. The sandwich for the small-prime coprimality indicator, multiplied by the atom's sign and by its divisibility indicator, is an upper bound termwise. The resulting pointwise sum therefore majorizes the rough-tree sum times that small-prime indicator, hence also the desired indicator by (4). Unique splitting at \(x^\eta\) gives coefficients of absolute value at most one. The fundamental lemma gives small-prime density \(V(x^\eta)(1+O(e^{-c/\sqrt\eta}))\). The absolute rough density is \(\ll1/\eta\); thus the attachment changes the density by \(O(e^{-c/\sqrt\eta}\eta^{-2}C_2/L)\). By (4), the product of the unrounded rough-tree density and \(V(x^\eta)\) is the full ideal density with only exits whose last prime is \(\ge x^\eta\); it is no larger than the full density. At fixed \(\eta\), the further alphabet discretization costs arbitrarily little on the \(C_2/L\) scale: (4), Mertens harmonic measure \(dt/t\), and the bounded rank reduce this to finite affine boundary strips in a compact region.

Reserve room in (5) for multiplying the third group by a small-prime factor of size at most \(x^{\sqrt\eta}\). Support as a whole is at most \(x^{5/8+\sqrt\eta}\), and rough ranks zero, one and two stay below \(x^{1/2-\epsilon_0}\) after decreasing \(\eta,\epsilon_0\). Choose a partition of each atom by its upper endpoints via the packing just proved. The squarefree indicator in a rough atom can be removed to get a product convolution: for each interval label of multiplicity \(m_J\), the original unrestricted convolution divided by \(\prod_J m_J!\) is exactly the ordered atom on squarefree moduli. Each group can separately be normalized by its own product of factorials, leaving an external fixed scalar; its product coefficients are bounded by one even on repeated primes. Small-prime attachment in group three does not change that bound by unique splitting. The introduced nonsquarefree rough terms cost at most
\[
x^{o(1)}\!\!\sum_{\substack{d\le x^{5/8+\sqrt\eta}\\\exists \ell\ge x^\eta:\,\ell^2\mid d}}
(x/d+1+x/\varphi(d))\ \ll\ x^{1-\eta+o(1)}
\tag{7}
\]
in the pair discrepancies, by the fixed prime-product divisor bound and summing multiples of each \(\ell^2\). An empty group is unit mass at 1. All residue coprimality restrictions factor into the groups.

## 4. Distribution on pairs of primes

For an integer \(n\) put
\[
\Delta_d(n)={\bf1}_{n\equiv2\ (d)}
 -{\bf1}_{(n,d)=1}/\varphi(d).
\]
Fix \(a_*>0\) and choose the reserves for the attached coefficients \(\rho_x(d)\) as in §3. Then for every \(A>0\)
\[
\sum_d\rho_x(d)\sum_{r,q\ {\rm prime}} w(r,q)\Delta_d(rq)
=O_A(xL^{-A}).
\tag{8}
\]
Here \(r,q\gg x^{a_*}\) for a fixed \(a_*>0\), \(rq=O(x)\), and \(w\) is a smooth geometric weight with mixed Euler derivatives bounded by fixed powers of \(L\). The coefficients, constructed with fixed reserves, do not depend on \(A\).

Fix the maximal divisor-function order \(K_{\rm mom}\) needed for the fixed Heath–Brown slots, modulus factors and squared coefficient bound. The saving \(A\) changes only logarithmic cutoffs and the number of integrations by parts. Choose \(0<\kappa<1/(2K_{\rm mom})\) subject also to the reserve bounds of §3. Smoothly discard products below \(2x^{1-\kappa}\). This costs \(x^{1-\kappa+o(1)}\) using \(\tau(rq-2)\) and \(\sum_{d\ll x}1/\varphi(d)\ll L\); the shift is nonzero because the primes exceed \(x^{a_*}\). On each remaining dyadic product chart \(X\gg x^{1-\kappa}\), the final support \(D_0\) is at most \(X^{5/8+\xi}\) with arbitrarily small fixed \(\xi>0\). For the charts and subcharts below, divisor moments with any fixed powers hold with only log losses: if \(n\asymp X\) then
\[
\sum_{n\asymp X} \tau(n)^j\tau(|n-2|)^k\ll X(\log X)^{O_{j,k}(1)}.
\tag{9}
\]
This is Cauchy–Schwarz and \(\tau^h\le d_{2^h}\), where \(d_j\) is the \(j\)-fold divisor function. On a prime power, the tuple of exponents is recoverable from the counts of each subset of coordinates that reaches each successive layer, proving the latter inequality. For an interval of length \(O(X)\) in \([1,O(x)]\), choose a largest factor of an ordered \(m\)-tuple. The other factors have product \(d\ll_m x^{1-1/m}\), and the last factor has \(O(X/d+1)\) possibilities. The divisor sum is \(O_m((X+x^{1-1/m})L^{m-1})\). The second term is controlled by \(x^{1-1/m}\ll X\) for \(m\le K_{\rm mom}\), by the choice of \(\kappa\). The same argument applies after the fixed shift by 2. Coprime means add at most \(O(L)\) using \(\sum_{d\le D_0}1/\varphi(d)\ll L\); the same sum with \(\tau(d)^J\) in the numerator is \(L^{O_J(1)}\), by \(d/\varphi(d)\le\tau(d)\).

For support \(D_0<X^{1/2-\epsilon_0}\), the required absolute average follows from the multiplicative large sieve. For completeness, after separating the two prime weights on chart lengths \(R,U\) with \(RU\asymp X\), expand in characters, cancel the principal character against the stated mean, and write each modulus \(d=gh\) with primitive conductor \(g>1\). Keep the auxiliary coprimality with \(h\) on both prime factors. For \(G<g\le2G\) the large sieve and Cauchy–Schwarz bound the conductor sum with coefficient \(1/\varphi(g)\) by
\[
L^{O(1)}\bigl(X/G+\sqrt X(\sqrt R+\sqrt U)+G\sqrt X\bigr).
\]
Indeed the two square-root factors take the form \(\sqrt{(R+G^2)R/G}\) and \(\sqrt{(U+G^2)U/G}\). For \(G>L^B\) sum dyadically and then use \(1/\varphi(gh)\le1/(\varphi(g)\varphi(h))\), \(\sum_h1/(h\varphi(h))<\infty\), and \(g\le D_0/h\); choose \(B\) large. For \(g\le L^B\) use prime Siegel–Walfisz, deleting primes dividing \(h\) at cost \(O(\omega(h)L^{O(1)})\). Both \(R,U\) are positive powers. This proves the small-support estimate.

On each original dyadic chart use a common threshold \(z_*=(C X_0)^{1/(\log\log(C X_0))^3}\), where \(X_0\) is its product scale and \(C\) a fixed constant larger than the ratios of all subsequent dyadic product endpoints to \(X_0\). This ensures \(z_*\ge X^{1/(\log\log X)^3}\) in its subcharts. Replace each prime indicator by \(\Lambda(m)/\log m\) with \(P^-(m)>z_*\) (set \(P^-(1)=\infty\)). In each dyadic scale \(R\gg x^{a_*}\) there are \(O(R^{1/2})\) proper prime powers, so pairing with the complementary scale \(V\asymp X/R\) and using \(\tau(|mn-2|)\le x^{o(1)}\) and \(\sum_{d\le x}1/\varphi(d)\ll L\) gives total discrepancy cost \(O(x^{1-a_*/2+o(1)})\). For each original length \(R_i\), put \(Z_i=(2R_i)^{1/3}\). With \(m_i=\mu{\bf1}_{[1,Z_i]}\), the order-three Heath–Brown identity here is
\[
\Lambda=\sum_{j=1}^3(-1)^{j-1}{3\choose j}m_i^{*j}*1^{*(j-1)}*\log
\qquad(n\le 2R_i).
\tag{10}
\]
This follows by expanding \((\delta-1*m_i)^{*3}*\Lambda\), which vanishes up to \(2R_i\), and using \(1*\Lambda=\log\). Factor the roughness over the at most six slots for each original prime, and subdivide each slot dyadically; truncated intervals remain in place. Mellin separation of the smooth geometric factor on these subcharts introduces only log-power costs: in logarithmic coordinates put a smooth compact cutoff around each dyadic interval and use Fourier inversion with two integrations by parts in each coordinate (arbitrarily many to truncate at \(|t|\le L^B\)). The integrable norm is \(L^{O(1)}\), and the truncated tail is negligible by (9). The individual twists have polylogarithmic derivatives. Absorb the log profile of a \(\log\) slot into this smooth separation, with an external log-power cost. The same separation justifies the use of one-variable prime Siegel–Walfisz in the small-support argument.

**A medium slot.** If some dyadic length \(U\in[X^{2\zeta},X^{1/3+\zeta/2}]\), take that coefficient for Pascadi's short side. It is a rough \(1\) or rough \(\mu\) times a twist and an interval. Rough \(1\) is Siegel–Walfisz: truncate inclusion–exclusion at the neighboring even and odd Brun degrees described below. Count multiples of the resulting \(d\le y_*=X^{o(1)}\) in each reduced class \(a\bmod q\) with \(q\) polylogarithmic. The two main terms differ by \(O_A(U L^{-A})\), and the error is at most \(y_*\) times a fixed log power; partial summation allows the twists. Rough \(\mu\) obeys the exact identity
\[
\mu(n){\bf1}_{P^-(n)>z_*}
=\sum_{\substack{d\mid n\\P^+(d)\le z_*}}\mu(n/d).
\]
For \(d>U^{1/2}\) the reciprocal mass is at most
\[
\exp[-\log U/(2\log z_*)]\prod_{\ell\le z_*}(1-\ell^{-1+1/\log z_*})^{-1}\ll_A L^{-A},
\]
by Rankin's inequality and Mertens. For the other \(d\), apply Möbius Siegel–Walfisz at lengths \(U/d\ge U^{1/2}\) and sum \(1/d\ll L\). Auxiliary coprimality with an integer \(h\) removes at most \(O((U/z_*+1)\omega(h))\) terms by roughness, in both proofs. If \(q>L^B\), one-boundedness gives \(O(U/q+1+U/\varphi(q))\). For \(q\le U^2\) use \(q/\varphi(q)\ll\log\log(3q)\ll\log L\) and take \(B\) large. For \(q>U^2\), \(\varphi(q)\ge\sqrt{q/2}>U/\sqrt2\), by multiplying the prime-power bounds \(\varphi(p^e)^2\ge p^e\) with the sole exception \(p^e=2\). Thus the error is \(O(1)\), admissible since \(U\ge X^{2\zeta}\). This verifies the full uniform condition. For the complementary coefficient, $|\beta_m|\le\tau(m)^C L^{C_0}$ for fixed $C,C_0$ independent of $A$. Truncating at $|\beta_m|\le L^{B_1}$ discards a tail bounded by $L^{-B_1}|\beta_m|^2\le L^{2C_0-B_1}\tau(m)^{2C}$; since $|\rho_x(d)|\le1$ and $d\mid um-2$ ($um\ne2$), summing over $n=um\asymp X$ gives progression error $\ll L^{2C_0-B_1}\sum_{n\asymp X}\tau(n)^{2C+1}\tau(|n-2|)$ and coprime-mean error $\ll L^{2C_0-B_1+1}\sum_{n\asymp X}\tau(n)^{2C+1}$, both $O_A(xL^{-A})$ by (9) once $B_1$ is chosen sufficiently large in terms of $A,C,C_0$ (with $K_{\rm mom}$ fixed earlier in terms of $C$ alone). Rescale the retained coefficient by $L^{-B_1}$ to be one-bounded, absorbing $L^{B_1}$ into the logarithmic accuracy of Pascadi's Proposition 4.4. The product scale stays \(MN\asymp X\) even after dyadically dividing the complementary product. Apply (5) to the packed atom, with dyadic subintervals in its three modulus groups. Their upper bounds suffice because all powers of \(Q_i\) in (5) are positive. The modulus coefficient with unit mass fits the chart of length \(1/2\). All losses are logarithmic. This establishes (8) for the medium case.

**No medium slot.** Choose \(\zeta\ll a_*\) so that each of the two original groups has a long slot of length \(>X^{1/3+\zeta/2}\): six short slots multiply to at most \(O(X^{12\zeta})\). There are exactly two long slots, because three of these lengths would have product \(>X^{1+3\zeta/2}\), and neither can be truncated Möbius since each original length is \(O(X)\). Thus the long coefficients are rough \(1\) times smooth profiles or twists, and the product of the short slots has scale \(M\le X^{24\zeta+o(1)}\), with \(L^1\)-norm \(O(M L^C)\) for a fixed \(C\). We can use absolute modulus averaging.

To see this, for fixed short product \(m\) coprime to \(d\), write \(b_0\equiv2\bar m\bmod d\). For smooth compact long profiles \(f_0,g_0\) of scales \(U,V\), double periodization yields the discrepancy for their unrestricted product:
\[
\frac{UV}{d^2}\sum_{j,k\in\mathbb Z}\widehat f_0(jU/d)\widehat g_0(kV/d)
\left(S(b_0j,k;d)-\frac{c_d(j)c_d(k)}{\varphi(d)}\right).
\tag{11}
\]
Here \(S\) is the complete Kloosterman sum and \(c_d\) a Ramanujan sum. Both axes vanish since \(b_0\) is a unit. For the other frequencies, \(|\widehat f_0(t)|\ll(\|f_0\|_1+\|f_0''\|_1)(1+|t|)^{-2}\); use the corresponding estimate for \(g_0\), and Weil's bound \(\tau(d)\sqrt d\,(j,k,d)^{1/2}\). For each common divisor \(h\mid d\), \(\sum_{j\ne0,h\mid j}(1+|j|/H)^{-2}\le2H/h\); the sum of \(h^{-3/2}\) converges. The Ramanujan term costs \(O(\tau(d)^2/\varphi(d))\) times the same profile norms, using \(|c_d(j)|\le(j,d)\) and applying the preceding bound separately in \(j,k\). Thus the summed error is \(O(MD_0^{3/2}L^{O(1)})\) by divisor moments. If \((m,d)>1\), both terms are zero. The factor \(MD_0^{3/2}\) has a fixed power saving because \(24\zeta+\tfrac32(5/8+\xi)<1\).

To restore roughness take \(h_0=2\lfloor(\log\log X)^2\rfloor\) and \(y_*=z_*^{h_0+1}=X^{o(1)}\). Taking divisors made of at most \(h_0\) or \(h_0+1\) distinct primes below or equal to \(z_*\) gives Brun polynomials \(U_z,L_z\) with \(L_z\le r_z\le U_z\), where \(r_z={\bf1}_{P^->z_*}\); the gap \(G_z=U_z-L_z\ge0\). All divisor coefficients are of absolute value at most one. If only divisors coprime to \(d\) are used, their upper reciprocal density \(a_d\) and gap density \(g_d\) satisfy \(a_d\ll1\) and \(0\le g_d\le\varepsilon_X=(\sum_{\ell\le z_*}1/\ell)^{h_0+1}/(h_0+1)!\ll_A L^{-A}\). This follows by inclusion–exclusion of independent events of probabilities \(1/\ell\). In a product, use \(0\le U_1U_2-r_1r_2\le G_1U_2+U_1G_2\) for the corresponding polynomials and indicators. Expanding two divisor coefficients in (11) changes \(U,V\) to \(U/e,V/e'\), shifts the short product to \(mee'\), and multiplies the preceding uniform discrepancy error by at most \(y_*^2\), still harmless. For the error in putting back the true indicators, take nonnegative smooth majorants for the profiles, and bound the discrepancy error by the discrepancy of the nonnegative gap majorant plus twice its coprime mean. For example,
\[
\sum_{(n,d)=1} f_0(n/U)U_z(n)
=U\frac{\varphi(d)}d a_d\int f_0+O(y_*\tau(d)(\|f_0\|_1+\|f_0'\|_1)).
\]
This is Möbius inversion of coprimality and the elementary arithmetic-progression sum–integral estimate. For \(G_z\) use \(g_d\) instead. The two long variables therefore give total gap means bounded by
\[
L^{O(1)}\bigl(MUV\varepsilon_X+M(U+V)y_*+My_*^2\bigr),
\]
which has arbitrary log saving since both long lengths are positive powers of \(X\) and \(MUV\asymp X\). For a sharp endpoint in a long slot of scale \(U\) (or \(V\)), replace the indicator by a smooth cutoff that differs only on strips of relative width \(h=L^{-B}\). The strip contains \(O(hU+1)\) integers, and the product of the other slot lengths is \(O(X/U)\). The set \(E\) of products of tuples from the strip thus has size \(O(X(h+U^{-1}))\), up to a fixed logarithmic factor. Estimate the smoothing error directly for the true rough sequences, without expanding the Brun majorants; tuple multiplicities and absolute coefficients are then bounded by \(L^{O(1)}\tau(n)^C\) for fixed \(C\). Before any modulus factorization, \(|\rho_x(d)|\le 1\) bounds the progression and coprime-mean errors together by \(L^{O(1)}\sum_{n\in E}\tau(n)^C(\tau(|n-2|)+L)\). Cauchy--Schwarz and the shifted divisor moments give \(O(X L^{O(1)}(h+U^{-1})^{1/2})\). Both long scales are positive powers of \(X\), so \(B\) can be chosen to give the required saving. Short-slot interval restrictions remain in the coefficient of the short product. This proves (8).

## 5. The density of the sieve

Normalize the linear-sieve functions by \(\mathcal F=F/(2e^\gamma)\) and \(\mathcal f=f/(2e^\gamma)\). The literal ordinary cubic Rosser upper and lower densities, divided by \(V(Y)\), tend to \(F(s)\) and \(f(s)\) at \(s=\log D/\log Y\), respectively for \(s>1\) and \(s\ge2\). We use this dimension-one exit-series form of the linear sieve for the fixed local density of (2), uniformly on compact parameter ranges. The normalized functions satisfy
\[
\mathcal F(s)=1/s\ (1\le s\le3),\qquad
\mathcal f(s)=0\ (s\le2),\qquad
(s\mathcal F(s))'=\mathcal f(s-1)\ (s\ge3),\qquad
(s\mathcal f(s))'=\mathcal F(s-1)\ (s\ge2).
\tag{12}
\]
\(\mathcal F\) decreases and \(\mathcal f\) increases to the same limit. The upper function is convex on \(s\ge1\): \(-\mathcal F'=(\mathcal F-\mathcal f(s-1))/s\) decreases. The lower function is concave on \(s\ge2\): \(\mathcal f'=(\mathcal F(s-1)-\mathcal f)/s\) decreases there. The kink at \(s=2\) in the extension of \(\mathcal f\) has upward derivative jump \(1/2\).

The ordinary tree of cap \(T\) has density \(2\mathcal F(T/\rho)/\rho=2/T+I_1\) in \(C_2/L\) units. In particular, setting \(h=T/\rho-3=1/8\),
\[
I_1=\frac{2}{T}\int_0^h\frac{\log(1+t)}{2+t}\,dt\ \le\frac{h^2}{2T}.
\tag{13}
\]
The third-prefix subtree is a negative copy of a lower cubic sieve, with remaining level exponent \(J-S_3\) and last-prime cutoff \(t_3\). If the third cube fails, this subtree is absent, exactly as expressed using \(\mathcal f(s)=0\) for \(s\le2\). Otherwise even descendants are free and odd descendants tested; the initial square rule of the lower residual sieve holds because \(J-S_3>2t_3\). Consequently the rank-three cap replacement adds
\[
I_3=2\int_{0<z<y<u<\rho}
\frac{\mathcal f((T-u-y-z)/z)-\mathcal f((J-u-y-z)/z)}
     {uyz^2}\,du\,dy\,dz .
\tag{14}
\]
The variables here are \(u=t_1,y=t_2,z=t_3\). The sign is nonnegative since \(J\le T\).

For rigor at the small-prime end, on the small-\(t_1\) branch (\(t_1<t_{1,\min}\) with fixed ordinary cap \(\lambda_{\rm small}<1/2\)) the odd prefix has negative sign and its residual tree tests even slots, so the residual sieve is the ordinary lower sieve. Choose \(t_{1,\min}\) small enough that \(\lambda_{\rm small}/t_{1,\min}-1\) exceeds \(9\) and the fixed threshold for the uniform large-\(s\) bound below. The absolute rank-one difference from \(T\) in normalized density is \(2\int_0^{t_{1,\min}}|\mathcal f(\lambda_{\rm small}/u-1)-\mathcal f(T/u-1)|\,u^{-2}\,du=O(t_{1,\min})\) since \(|\mathcal f(s)-1/(2e^\gamma)|\le \mathcal D(s)\ll s^{-2}\) for \(s\ge 9\), while (14) over \(u<t_{1,\min}\) is \(O(t_{1,\min}(1+\log^2(\rho/t_{1,\min})))\). For the discrete sums, the one-sided Rosser bound ([Suzuki, Lemma 14.7](https://www.suzuyu1729.com/notes/NagoyaSeminar2022/RosserIwaniec.pdf)), the lower-sieve inequality \(V^-(D,y)\le V(y)\), and \(1-f(s)\ll s^{-2}\) give \(0\le V(y)-V^-(D,y)\ll V(y)s^{-2}\) uniformly for large \(s=\log D/\log y\). Indeed, with the sieve dimension and constants fixed, the lemma gives an error bounded by \(V(y)CE(s)(\log D)^{-\Delta}\) for some fixed \(\Delta>0\), where \(E(s)\le\exp(-s\log s+s\log\log(3s)+O(s))\) for all \(s\ge1\). This is \(O(V(y)s^{-2})\) since \(E(s)\ll s^{-2}\) and \(\log D\ge\log 2\). At \(y=x^u\) this bounds the rank-one residual difference by \(O(C_2u/L)\); dyadic summation with the harmonic prime measure bounds the total by \(O(t_{1,\min}C_2/L)\).

On \(z<\delta'\) (\(t_1\ge t_{1,\min}\)), all approximations keep \(J-t_1-t_2\) bounded below by a uniform positive constant, so both residual densities agree with \(V(x^z)\) up to \(O(V(x^z)z^2)\) by the same uniform lower-sieve bound and their difference is \(O(C_2z/L)\); integrating the harmonic measures gives \(O(\delta'(1+\log^2(\rho/\delta'))C_2/L)\). On \(z\ge\delta'\), \(t_1\ge t_{1,\min}\), the cubic residual limit and harmonic measure \(dt/t\) give (14), while trimming switching walls, replacing small \(t_3\) by the fallback, taking \(\rho'\uparrow\rho\), lowering physical caps, and restricting the compact rank-four domain (17) (\(t_4\ge3/100\)) each change the limiting density by arbitrarily little. Thus the un-discretized full finite policy \(\mathcal T_{\rm full}\) has density at most \((U_0+u_0+o(1))C_2/L\) (or minus \(G_1\)). By (4), \(V(x^\eta)\) times the un-discretized rough-tree density \(\mathcal T_{\rm rough}^{(0)}\) isolates exits with last prime \(\ge x^\eta\) and is at most the density of \(\mathcal T_{\rm full}\); choosing \(\eta\) sufficiently small keeps the attachment error at most \(\tfrac12 u_0 C_2/L\), and then refining the common alphabet at fixed \(\eta\) keeps the discretization difference between \(\mathcal T_{\rm rough}\) and \(\mathcal T_{\rm rough}^{(0)}\) at most a further \(\tfrac12 u_0 C_2/L\), giving total density at most \((U_0+2u_0+o(1))C_2/L\) (or minus \(G_1\)).

For a sharp explicit tail in (14), set \(\delta=19/1000\) and \(\mathcal D=\mathcal F-\mathcal f\). From (12),
\[
\mathcal D'(s)=(-\mathcal D(s)-\mathcal D(s-1))/s
\ \le -2\mathcal D(s)/s \quad (s\ge3).
\tag{15}
\]
Since \(J-u-y\ge(1-3\rho)/2=\rho\), the lower argument in (14) is at least \((\rho-\delta)/z>9\) for \(z<\delta\). Its numerator is at most \(\mathcal D(9)81z^2/(\rho-\delta)^2\): use (15) and the common limiting value of the two functions. Integrating the ordered larger coordinates gives at most \(\tfrac12\log^2(\rho/z)\). Thus if \(I_{3,c}\) is (14) over \(z\ge\delta\), the remaining \(I_{3,t}\) satisfies
\[
I_{3,t}\ \le\ \frac{81\mathcal D(9)\delta}{(\rho-\delta)^2}
\left(\log^2(\rho/\delta)+2\log(\rho/\delta)+2\right).
\tag{16}
\]
The unrounded rank-three bound is \(U_0=2/T+I_1+I_{3,c}+I_{3,t}\); there is no top interval using solely \(v(t_1)\) because \(\rho<1/4\).

At rank four the residual is a **positive** upper tree, so increasing the cap subtracts the nonnegative gain
\[
G_1=2\int_{\mathcal A}
\frac{\mathcal F((J-S_4)/t_4)-\mathcal F((M-S_4)/t_4)}
{t_1t_2t_3t_4^2}\,dt_1\,dt_2\,dt_3\,dt_4 .
\tag{17}
\]
Here \(\mathcal A\) consists of ordered prefixes with \(t_4\ge3/100\) which pass the third cube and have an admissible improvement (3). The residual arguments exceed 1: \(J>S_2+3t_3\) implies \(J-S_4>2t_3-t_4\ge t_4\). The factor 2 in (13)–(17) comes from (2) and the normalization in (12).

## 6. Applying the upper sieve to the bad pairs

Let \(K\) be any upper bound for \(U_0+2u_0\) or for \(U_0+2u_0-G_1\), as appropriate. The coefficients majorize the sifted indicator and have density at most \((K+o(1))C_2/L\). For every row fix \(a_*=1/3\) before constructing \(\rho_x\). Discard \(p<x/L^B\) for fixed \(B>4\), at cost \(O(x/L^B)\). The remaining pairs satisfy \(rq\ge x/L^B\) and \(r>(rq)^{b/(1+b)}\), giving \(q\ge r\gg x^{a_*}\) because \(b/(1+b)>1/3\). Since \(p>x^{\rho'}\), apply the pointwise upper bound to \(p=rq-2\). Use nonnegative smooth majorants of the pair region, then (8). The cost of replacing its coprime mean by the unrestricted pair mass times \(\sum_d\rho_x(d)/\varphi(d)\) is negligible: \(\sum_{d\le 2x,\ \ell\mid d}1/\varphi(d)\ll L/\ell\) for each \(\ell=r,q\). This follows from \(\varphi(\ell m)\ge(\ell-1)\varphi(m)\).

For detail on the majorants, set \(t=\log r/L,\ y=rq/x,\ \beta_b=b/(1+b)\). On \(y\ge\sigma>0\), the domain in \(t\) differs from \(\beta_b<t\le1/2\) only by \(O_\sigma(1/L)\) at the endpoints, and \(y\le1+2/x\). Approximate from above with smooth outer functions in \(t,y\) of arbitrarily small fixed width; these have polylogarithmic Euler norms. For \(y\le\sigma\) use a smooth positive majorant supported on \(y<2\sigma,\ r\in[x^{\beta_b-o(1)},2\sqrt x]\), with the lower product cutoff \(x/L^B\) smoothly inserted. Equivalently, take fixed slightly enlarged lower \(t\)-bounds and a smooth product cutoff at a fixed fraction of \(x/L^B\); the transition has bounded Euler norms. On the positive compact regions, the prime number theorem in \(q\) and the prime harmonic measure in \(r\) give limiting measure \(dt\,dy/[t(1-t)]\) after dividing the pair mass by \(x/L\). The small-\(y\) majorant has mass \(O(\sigma x/L)\): \(q\le2\sigma x/r\), the prime number theorem bounds the number of such primes by \(O(\sigma x/(rL))\), and the harmonic prime sum over \(r\) in this positive exponent range is bounded. In all applications one also imposes positive exponent bounds on both slots, without removing any required pair. Let the smoothing width and then \(\sigma\) tend to zero. The total limiting mass is
\(\int_{\beta_b}^{1/2}dt/[t(1-t)]=\log(1/b)\). It follows that
\[
\limsup_{x\to\infty} B_b(x)/H(x)\le K\log(1/b),\qquad
\liminf_{x\to\infty} A_b(x)/H(x)\ge12759/10000-K\log(1/b).
\tag{18}
\]

## 7. Directed certificate

The standalone `verify_twin_upper_sieve_cert.py` checks the following bounds at denominator \(Q=2^{80}\). Its only arithmetic in bounds is integer arithmetic, including `Fraction` for exact rational numbers, `isqrt` for upward-rounded square roots, and floor and ceiling divisions to convert to denominator \(Q\).

1. **Logs and delay equations.** The series for \(\log x\) at \(v=(x-1)/(x+1)\) is \(2\sum_{j\ge0}v^{2j+1}/(2j+1)\); the remainder after \(m\) terms is nonnegative and at most \(2v^{2m+1}/((2m+1)(1-v^2))\) for \(1\le x\le2\). Reduce larger arguments by powers of 2. The delay table uses \(s\mathcal F,s\mathcal f\) on the \(1/n\) mesh, \(n=4096\). In integrating the preceding numerator's chord against \(ds/s\) by (12), the positive weights are \((j+1)\log(1+1/j)-1\) and \(1-j\log(1+1/j)\) on \([j/n,(j+1)/n]\); the terms are \((-1)^{m+1}/(m(m+1)j^m)\) and \((-1)^{m+1}/((m+1)j^m)\). Fourth and fifth partial sums bound them outward. By (12), \(|\mathcal F'|,|\mathcal f'|\le1\) in their active ranges above 1 and curvature of a numerator is bounded by 1 where integrated, inside each mesh cell. The numerator \(s\mathcal F\) is **convex** and \(s\mathcal f\) **concave**; hence the integrated chord correction is at most \(1/(12n^2j)\), subtracted in the lower bound for the next \(s\mathcal f\) only if the \(s\mathcal F\) cell is nonconstant, added in the upper bound for the next \(s\mathcal F\). A chord pointwise error is at most \(a(h-a)/2\) at distance \(a\) within a cell of width \(h\). Beyond 12 both normalized functions are enclosed by \([\mathcal f(12),\mathcal F(12)]\). An independent high-precision test uses quarter intervals with local parameter \(t\in[0,1]\). With delay polynomial \(P\) and \(j=4(s_{\rm left}-1)\), integrate \(P(t)\sum_{m=0}^{43}(-1)^m t^m/j^{m+1}\). The uniform numerator error propagated per interval is at most the previous endpoint error plus the delayed error divided by \(j\), plus \(\|P\|_{\ell^1}/j^{45}\) and the accumulated outward coefficient rounding. This reference encloses both branches at all integers 4 to 12 to within \(10^{-12}\) in numerator units and checks containment in the main table.

2. **Geometry.** A cell intersected with decreasing coordinate order is an ordered simplex on each run of \(m\) identical intervals \([l,h]\), with \(1/m!\) of the box volume, centroid positions \(l+j(h-l)/(m+1)\) in increasing order, and coordinate variances at most \((h-l)^2/12\). These facts follow by the uniform order-statistic law, whose \(j\)-th marginal after scaling to \([0,1]\) has beta density proportional to \(t^{j-1}(1-t)^{m-j}\). Separate runs are independent. Midpoint subdivision splits a run by the number of coordinates above the midpoint, exactly covering its parent. All endpoints, centers and affine expressions have an integer representation. For an affine form \(Y\), its mean positive part is at most \((\sqrt{\operatorname{Var}(Y)+(\mathbb EY)^2}+\mathbb EY)/2\); use Cauchy–Schwarz within each run, independence across runs, and the relaxed bound \(\sqrt{12}>17/5\).

3. **Kinks and eligibility.** A cap is the minimum of one or two affine planes, possibly with strict affine guard tests against both planes. In (14) use only a cap whose guards hold throughout the cell; choose the greatest central value of these. For its central-active plane \(P\), the overestimate of the cap is the positive part of \(P-P_{\rm other}\). Correct this by a bound for its mean positive part, multiplied by a slope bound at a certified lower residual argument. For (17) enforce the third cube using a uniform affine minorant of a guaranteed parent cap, lowering its central-active plane by its worst possible kink error. For each possible parent cap take its central-active plane as a majorant; discard a guarded cap from this list only when a strict test is impossible on that cell. The greatest central plane \(P\) then bounds the old cap above up to the sum of mean positive parts of the other central-active planes minus \(P\). For the new tent, certify (3) for both planes throughout the cell and subtract the possible kink cost. If the new cap fails to improve the old at some point, the actual gain at that point is zero and is still at least the signed comparison. The arithmetic uses only the greatest certified lower bound of the proposed new caps on a cell, not their sum. In these comparisons extend \(\mathcal F(s)=1/s\) for \(0<s\le1\) and reject a lower-bound cell if the needed positive residual bounds cannot be established.

4. **Directed integral within a cell.** For a proxy affine cap \(P\) write \(s=(P-S_d)/t_d\), \(\mathbf c\) for the centroid, and \(g=P-S_d-s(\mathbf c)t_d\), which is affine with mean zero. Let \(B(\mathbf t)=2\prod_i t_i^{-a_i}\), \(a_i=1+{\bf1}_{i=d}\). If \(l_i\) are lower endpoints and \(\sigma_g,\sigma_i\) standard deviation bounds, the weighted linear Taylor error for a function \(\phi=\mathcal F,\mathcal f\) is bounded in magnitude by
   \[
   B(\mathbf l)\frac{|\phi'(s(\mathbf c))|\sigma_g}{l_d}
        \sum_i(a_i+{\bf1}_{i=d})\frac{\sigma_i}{l_i}.
   \]
   Indeed, subtract the constant \(B(\mathbf c)/c_d\) from \(B/t_d\) inside the integral of the centered affine form and use Cauchy–Schwarz and the derivative bounds for \(B/t_d\). In a difference of branches use the smaller of the separate estimate and the joint standard deviation bound for \(d_1g_1-d_2g_2\), at centered slopes of magnitudes \(d_1,d_2\): either \(d_1\sigma_{g_1-g_2}+|d_1-d_2|\sigma_{g_2}\) or its counterpart with \(d_2\). The quadratic correction costs at most \(B(\mathbf l)\sup|\phi''|\sigma_g^2/(2l_d^2)\) in the direction not already provided by convexity or concavity. Equation (12) yields \(|\phi''|\le(|\psi'(s-1)|+2|\phi'|)/s\), where \(\psi\) is the other branch. Across \(s=2\) in the lower function the lower Taylor bound stays valid, while the upper estimate can need an additional \(B(\mathbf l)\sigma_g/(4l_d)\): the derivative jump is \(1/2\) and the mean positive or negative part of a centered affine form is at most half its standard deviation. Finally \(\mathbb EB\ge B(\mathbf c)\) by convexity and
   \[
   \mathbb EB\le B(\mathbf c)+\frac{B(\mathbf l)}2
   \left[\left(\sum_i a_i\sigma_i/l_i\right)^2+\sum_i a_i(\sigma_i/l_i)^2\right]
   \]
   by its Hessian. The arithmetic uses these bounds for the common weight once, rounds upper endpoints up and lower endpoints down, and multiplies by the exact cell volume. Subdivision scores do not enter the certified sum.

### Certified values

The reference uses \(T=5/8\) as a density comparator, not as an analytically admissible exact level. Trying \(T=0.60,0.612,0.625\) did not change the ideal combined density except for quadrature error, as expected from the exact third-rank comparison when the first cube always passes. Increasing \(\rho\) from \(0.1875\) toward \(0.20\) improved that density. The proof takes its limit at \(1/5\) with strict reserves obtained at \(\rho'<1/5\). Use \(u_0=1/10^6\) for each of the two approximation allowances.

Run `python verify_twin_upper_sieve_cert.py`. All table entries are exact numerators with denominator \(Q=1208925819614629174706176\).

| Quantity | Direction | Numerator |
|---|:---:|---:|
| \(I_1\) | \(\le\) | 13943390692550619486377 |
| \(I_{3,c}\) | \(\le\) | 66925635371004488689726 |
| \(I_{3,t}\) | \(\le\) | 3409294078124169319 |
| \(G_1\) | \(\ge\) | 19374509949983140898664 |
| \(K_3\), upper bound for \(U_0+2u_0\) | \(\le\) | 3949437475976085820663535 |
| \(K_4\), upper bound for \(U_0+2u_0-G_1\) | \(\le\) | 3930062966026102679764871 |

The compact integrals use 435001 and 700001 box/simplex evaluations respectively, including parents that were later divided. The following are lower bounds from (18) (from §1 for the first row), in the same denominator:

| \(b\) | Sieve | Margin numerator |
|---|---|---:|
| \(3539/5000\) | two-factor shortcut | 377883443722357593132 |
| \(6767/10000\) | rank three | 105553009773095358394 |
| \(17/25\) | ranks three and four | 26790620021371983365686 |
| \(169/250\) | ranks three and four | 3604340579464536079328 |
| \(3377/5000\) | ranks three and four | 114570068060210771664 |
| \(67539/100000\) | ranks three and four | 56380964408304863785 |
