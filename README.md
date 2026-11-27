# Proposition $(1 - 1.67440)$ on Twin Primes

**Author:** Wei Lindong (Independent Researcher, [ORCID 0009-0008-9652-2845](https://orcid.org/0009-0008-9652-2845)) · **Code license:** MIT · **Manuscript / PDF license:** CC BY 4.0

**Version 1.0.3.** For all sufficiently large $x$, more than
$0.0000466\,C_2x/(\log x)^2$ primes $p\le x$ satisfy
$$
p+2=rq,\qquad q\text{ prime},\qquad r\in\{1\}\cup\mathbb P,
\qquad r\le q^{0.67440},
$$
where $C_2=2\prod_{\ell>2}(1-(\ell-1)^{-2})$.

The delayed four-slot sieve and [Ibarra's Chen lower bound](https://doi.org/10.5281/zenodo.24545780)
strengthen the baseline four-slot result from $1-1.67539$ to $1-1.67440$.
This also improves [Li and Liu's $1-1.75$](https://arxiv.org/abs/2606.05224v2)
by $0.07560$ in the exponent.

| Construction | Proposition | Bound on $r$ |
|---|---:|---:|
| Li–Liu, Theorem 1.2 | $1-1.75$ | $r\le q^{0.75}$ |
| Two-factor shortcut | $1-1.7078$ | $r\le q^{0.7078}$ |
| Rank three | $1-1.6767$ | $r\le q^{0.6767}$ |
| Baseline ranks three and four | $1-1.67539$ | $r\le q^{0.67539}$ |
| **Delayed four-slot sieve, Theorem 1.1** | **$1-1.67440$** | **$r\le q^{0.67440}$** |

**Scope distinction:** Baker and Harman (1996) proved $P^+(p+2) > p^{0.676}$ infinitely often ($p+2=rq$ with $r \le q^{0.48}$), where $r$ is a general composite integer not restricted to $\mathbb{P} \cup \{1\}$. The present theorem keeps Chen's $\Omega(p+2) \le 2$ restriction ($r = 1$ or prime). Like all one-sided linear sieve subtractions, this framework remains subject to the parity barrier and does not reach the twin prime conjecture $(1 - 1)$.

## Reproducing the certificate

Run from the repository root with Python 3.10 or newer and `g++` supporting
C++20 and `__int128`.

~~~bash
python w4/verify_w4_certificate.py --recompute-baseline
~~~

The command regenerates the directed sieve table, evaluates **8,500,001**
ordered boxes for the additional gain, and independently reruns the original
Python certificate. The original verifier can also run by itself using Python's
standard library.

At denominator $Q=2^{80}$, the checked numerators are

| Quantity | Direction | Numerator |
|---|---:|---:|
| Total four-slot gain $G_1+\Delta G_1$ | $\ge$ | 19598258419400386998038 |
| Delayed four-slot density bound $K_{\rm W4}$ | $\le$ | 3929839217556685433665497 |
| Final margin at $b=0.67440$, $c_{\rm low}=1.2806$ | $\ge$ | 61483810070100487491 |

The final margin exceeds $0.0000466$. The [audit](W4-certificate-review.md)
details the packing branches, the full baseline cap in the incremental
integral, and the $2u_0$ density allowance.

## Manuscript and supporting files

- [paper.pdf](paper.pdf) is the 14-page manuscript. [arxiv-src.zip](arxiv-src.zip) contains the matching `paper.tex` with its bibliography inline.
- [TwinPrime-1-minus-a-SelfContained.md](TwinPrime-1-minus-a-SelfContained.md) is the Markdown proof.
- [w4/](w4/) contains the box evaluator, table generator, [replay driver](w4/verify_w4_certificate.py), and [full run log](w4/verify_output.txt).
- [verify_twin_upper_sieve_cert.py](verify_twin_upper_sieve_cert.py) and [verify_output.txt](verify_output.txt) are the baseline verifier and its archived run log.
- [submission-metadata.md](submission-metadata.md) contains submission fields for this revision.

Rebuild the PDF with `build.ps1` on Windows or run `pdflatex paper.tex`
three times with a standard TeX Live installation.

## External inputs and acknowledgments

[Runbo Li, Theorem 1.3](https://arxiv.org/abs/2405.05727v4) supplies the baseline
$1.2759$ Chen lower bound, and [Ibarra, Theorem B](https://doi.org/10.5281/zenodo.24545780)
supplies $1.2806$ for the main theorem. The distribution input is
[Pascadi, Proposition 4.4](https://arxiv.org/abs/2505.00653v1).
[Chan's Goldbach preprint](https://aixiv.science/pdf/aixiv.261111.000001v1.0.pdf)
provides the methodological precedent for the positive prefix sieve and the
subtraction of excluded semiprimes. The derivation and implementation were
developed in an AI-assisted, human-directed workflow. Both certificates were
rerun in a separate audit.

## Archive and citation

Source repository: [wellingtonthu/twin-primes-1-67539](https://github.com/wellingtonthu/twin-primes-1-67539).
This release is archived as [Zenodo v1.0.3](https://doi.org/10.5281/zenodo.24582753).
The previous published $1-1.67539$ manuscript is archived at
[Zenodo v1.0.2](https://doi.org/10.5281/zenodo.24552165)
and [aiXiv v1.3](https://aixiv.science/pdf/aixiv.261125.000002v1.3.pdf).
Use the [concept DOI](https://doi.org/10.5281/zenodo.24539532) for the project across archived
versions. See [CITATION.cff](CITATION.cff) for citing this release.
