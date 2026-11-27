# 四阶贪心分支的覆盖证明与数值证书

基线为本地提交 8d8f12d 的旧筛树与整数证书。使用 Ibarra Theorem B 的输入 $c=1.2806$。本研究保持四阶截断 $t_4\ge 3/100$。原基线验证器保留原样。独立复算程序和正文修订仅写入 w4-1.67440 工作树。

## 1. 分支条件

令 $S_j=\sum_{i\le j}t_i$，$T=5/8$。记 $J$ 为原三阶上限，$M$ 为原四阶上限，包括继承的 $J$。定义
\[
A_j=T-\frac38t_j,\quad B=1-2t_2,\quad W_4=\min(A_4,B).
\]
在 $t_4\ge 3/100$ 且 $t_1+t_2+3t_3<J$ 的有序域上，使用 $M'=\max(M,W_4)$。其他参数区域使用旧规则。严格切换条件为 $W_4>M$。仅在此时执行新分支，故 $W_4>M\ge J\ge(1+t_1)/2$。

原先额外提出的守卫 $1-t_2-2t_3$ 自动冗余。由排序，
\[
\frac53(t_2+2t_3)\le t_1+t_2+3t_3<J\le T.
\]
因此 $t_2+2t_3<3/8$，而 $W_4\le 5/8-9/800$。这个推导给出了四阶紧域上的固定间隙。

## 2. 全部装箱情形

沿用原 Lemma 3.1 的记号。设物理上限低于覆盖指数 $\ell$，且覆盖指数低于 $W_4$。令
\[
D=X^{\ell-2\zeta},\quad A=UX^{-\zeta},\quad
b_-=2\ell-1,\quad b_+=\frac{2-2\ell}{3},\quad
B_0=X^{b_-},\quad C=\frac{D}{AB_0}.
\]
在有限盒和尺度转换中保留共同正余量，使 $t_1<b_-$、$2t_2<1-\ell-2\zeta$、$t_2+2t_3<1-\ell-2\zeta$、$t_4<b_+-b_-$。前四个全平方约束由继承的第三槽测试及前两槽的原余量提供。后续全平方约束由新物理上限下的奇数槽立方测试提供。因而每个槽都满足 $S_{j-1}+2t_j\le \ell-\delta$，其中 $\delta>4\zeta$。以下以槽的上端点作装箱。

1. 若 $C<1$，用旧两组修复 $(A,D/A,1)$。全平方约束防止两组同时拒收。因为 $D/A<B_0$，第二个解析单项式不超过按 $B_0$ 估计的值。第一个为 $U^2D/A\le X^{23/24-\zeta/2}$。
2. 若 $C\ge 1$，第一槽放进第二组，第一和第三组初始容量积为 $X^{1-\ell-2\zeta}$。第二槽可放入其中一组。放入后剩余容量之积为 $X^{1-\ell-2\zeta-t_2}$，大于第三槽大小的平方。第三槽也可放入这两组之一。两次任选适容的组即可。
3. 继续贪心。若没有失败，第二组容量指数取 $b_-$。若首个失败槽为 $j\ge4$，记大小为 $X^s$，放入前各组部分乘积为 $a_i$。由于三组均拒收，$B'=a_2 X^s>B_0$；同时 $B'\le B_0 X^{t_4}<X^{b_+}$。由 $A<a_1 X^s$ 和 $a_1a_2a_3 X^{2s}\le D$ 得 $AB'a_3<D$。因此冻结第二组并重设第三组容量 $D/(AB')$，已放入的槽仍适容。后续若第一和第三组同时拒收，则其剩余容量之积小于当前槽大小的平方，与全平方约束矛盾。
4. 三组情形的两个解析单项式分别为 $X^{2\zeta}D^2/B'$ 和 $X^{2\zeta}D^2(B')^3$，其中无失败时以 $B_0$ 代替 $B'$。因 $b_-\le\log_X B'\le b_+$，二者分别不超过 $X^{1-2\zeta}$、$X^{2-2\zeta}$。$Q_1=A$ 已有固定节省。小素数筛权继续附加在第三组，以原有方式从节省中支付。

覆盖了空第三组、无失败、首次失败恰在第四槽、首次失败更晚。若只有三个粗槽，沿用旧构造。第三槽立方测试失败时，四阶分支不可复活该前缀。无中等变量的分析分支只依赖总支持，旧界继续适用。

## 3. 全域符号和边界

原三阶贪心端点 $W_3=\min(A_3,B)$。对所有有序向量，$A_4\ge A_3$，所以 $W_4\ge W_3$。严格大于当且仅当 $t_4<t_3$ 且 $B>A_3$。$B\le A_4$ 时新端点由 $B$ 决定，$B\ge A_4$ 时由 $A_4$ 决定，等号处相同。

对任一旧双仿射候选，记两个平面为 $p_1,p_2$，各严格守卫右端为 $g_j$。其有效充要条件为每个 $p_i>g_j$。当它有效时，$W_4>\min_i p_i$ 当且仅当至少一个 $p_i$ 同时严格小于 $A_4,B$。对所有有效旧候选取合取，连同第三槽测试及四阶截断，就得到新旧分支的完整切换条件。旧候选带来的上限等于新上限时可沿用旧分配。$v$ 的两平面在和等于 $1/4$ 时取同值。严格守卫等号按未通过处理。初始第三组容量等于 1 可走三组证明，适容测试允许等号。

连续积分中，排序面、截断面、守卫墙、立方墙和非恒等的仿射切换面都没有体积。离散构造在不能保留严格余量的盒上沿用旧规则，不删计数。若比较恒等，在整个盒上仍可沿用旧规则。裁剪后紧域上的共同余量可按旧方法在网格舍入、$x$ 到 $X$ 的尺度转换及小素数附件前选定。新增域紧致且被积函数有界，故裁剪可纳入原 $u_0$ 预算，附件和舍入仍在第二个 $u_0$ 内。

## 4. 额外四阶收益

在四阶域 $\mathcal A_4$ 上，令 $s_M=(M-S_4)/t_4$、$s_W=(W_4-S_4)/t_4$。第三槽通过时 $s_M>1$。额外收益为
\[
\Delta G_1=\int_{\mathcal A_4}\frac{2}{t_1t_2t_3t_4^2}
\begin{cases}
\widetilde F(s_M)-\widetilde F(s_W),& W_4>M,\\
0,&W_4\le M
\end{cases}
\,d\mathbf t.
\]
这直接以旧四阶规则作基线。用 $J$ 代替 $M$ 会重复计入旧四阶节省。$\Delta G_1$ 处处非负，$G_1'=G_1+\Delta G_1$。旧三阶证书上界不受影响。

经 8,500,001 次有序盒评估，以 $10^{24}$ 为分母，得到 $\Delta G_1$ 的向外端点 185080395990360007633 和 311314004869422725676。以 $Q=2^{80}$ 为分母时，
\[
 G_1'\ge \frac{19598258419400386998038}{Q},\qquad
 K'\le\frac{3929839217556685433665497}{Q}.
\]
对 $b=0.67440$，现有对数上界给出余量至少 $61483810070100487491/Q>0.0000466$。对 $b=0.67439$，余量至少 $3211740769042638632/Q>0$。后一行还没有认证原密度声明。

## 5. 定向盒界及复算

将域划为有序单元。每个相同区间的连续组若有 $m$ 个坐标，其体积为相应盒体积除以 $m!$。对每个旧候选的全部仿射守卫作向外极值测试。只在证明全盒不通过时从可能集合移除，只在证明全盒严格通过时加入保证集合。立方测试采用同样的两向分类。穿墙盒若无法保证第三槽通过，下界记零，上界覆盖全盒。变长细分只切分一个连续相同区间组，枚举落在上半区间的坐标数，形成不重叠的有序子单元。

设候选由平面集合 $P$ 定义，新计划由平面集合 $W=\{A_4,B\}$ 定义。对该候选，差额 $W_4-\min P$ 的下界可取 $\min_{w\in W}\max_{p\in P}\inf(w-p)$，上界可取 $\max_{p\in P}\min_{w\in W}\sup(w-p)$。旧上限取最大，故对可能集合取最小下界，对保证集合取最小上界，得到 $d_L,d_U$。若 $d_U\le0$ 即可记零。用仿射分式极值同时夹住 $s_M,s_W$。在增益非零时，单调性给出由函数端点相减得到的区间，凸性给出由 $d_L/(t_4)_U$、$d_U/(t_4)_L$ 和 $-\widetilde F'$ 的相反方向端点相乘得到的区间，可以取两者交集。盒上积分权重用坐标乘积的端点夹住。函数表超出末点的情况沿用原证书的极限夹逼，斜率下界可用零。

以下表生成器使用现有 Python 证书的延迟表及斜率区间。将两个附录分别存为 make_table.py 和 ordered_boxes.cpp，在独立目录执行 python make_table.py <现有验证器的路径>，再用 C++20 编译 ordered_boxes.cpp（要求编译器支持 128 位整数）。以参数 8500000 执行所得程序。输出三列依次是评估数、下界整数、上界整数，随后是分母。初始划分为每轴 16 等分。相同优先级按坐标字典序处理，可精确复现上面的整数。

从本工作树根目录运行以下命令可复跑分支证书，并核对原验证器的基线。

~~~powershell
python w4/verify_w4_certificate.py --recompute-baseline
~~~

结果记录在 [w4/verify_output.txt](w4/verify_output.txt)。

### 附录 A：整数表生成器
~~~python
from pathlib import Path
import runpy
import sys

v = runpy.run_path(sys.argv[1])
v["at"].__globals__["TAB"] = v["sieve_table"]()
q, n = v["Q"], v["n"]
rate = 10**12
with Path("sieve_table.txt").open("w") as f:
    for i in range(n, 12*n + 1):
        a, b = v["at"](0, i, n)
        l, u = v["at_slope"](0, i, n, a, b)
        print(a*rate//q, -(-b*rate//q), l*rate//q, -(-u*rate//q), file=f)
~~~

### 附录 B：独立整数组合验证程序
~~~cpp
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
~~~
