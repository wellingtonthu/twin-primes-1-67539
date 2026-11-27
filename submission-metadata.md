# Submission metadata (arXiv / aiXiv / journal forms)

Copy-paste fields for the upload forms. Values match `paper.tex` and `paper.pdf`.

## Title

A Self-Contained Proof of Proposition (1-1.67440) for the Twin Prime Problem

## Short title (running head, if asked)

Proposition (1-1.67440) for Twin Primes

## Author

- Name: Wei Lindong
- Affiliation: Independent Researcher
- Email: 744140495@qq.com
- ORCID: 0009-0008-9652-2845

## arXiv classification

- Primary: math.NT (Number Theory)
- Cross-list: none
- MSC 2020: 11N36 (Primary); 11N05, 11P32

## Keywords

twin prime problem, Chen's theorem, weighted sieve, level of distribution, directed integer certificate

## Abstract (plain text)

For 1 <= a <= 2, Proposition (1-a) asserts that there exist infinitely many primes p such that p+2 = rq with q prime, r = 1 or prime, and r <= q^(a-1). Li and Liu recently established Proposition (1-1.75) unconditionally. We combine Ibarra's lower bound pi_(1,2)(x) > 1.2806 C_2 x/(log x)^2 (improving Runbo Li's published 1.2759 bound) with a self-contained positive upper-sieve majorant at distribution level 5/8, a delayed four-slot refinement, and directed integer certificates. We prove Proposition (1-1.67440) unconditionally. For all sufficiently large x, more than 0.0000466 C_2 x/(log x)^2 primes p <= x admit the stated factorization with r <= q^0.67440. The two-factor shortcut, the rank-three construction, and the baseline four-slot construction give exponents 1.7078, 1.6767, and 1.67539, respectively.

## Abstract (LaTeX, for forms that accept it)

For $1 \le a \le 2$, Proposition $(1-a)$ asserts that there exist infinitely many primes $p$ such that $p+2 = rq$ with $q$ prime, $r=1$ or prime, and $r \le q^{a-1}$. Li and Liu recently established Proposition $(1-1.75)$ unconditionally. By combining Ibarra's lower bound $\pi_{1,2}(x) > 1.2806\,C_2 x/(\log x)^2$ (improving Runbo Li's published $1.2759$ bound) with a self-contained positive upper-sieve majorant at distribution level $5/8$, a delayed four-slot refinement, and directed integer certificates, we prove Proposition $(1-1.67440)$ unconditionally. More precisely, writing $A_b(x)$ for the number of primes $p \le x$ satisfying $p+2 = rq$ with $r \le q^b$, we obtain $A_{3372/5000}(x) > 0.0000466\,C_2 x/(\log x)^2$ for all sufficiently large $x$. We also record an elementary two-factor shortcut yielding Proposition $(1-1.7078)$, a rank-three baseline yielding Proposition $(1-1.6767)$, and the baseline four-slot bound $(1-1.67539)$.

## Release candidate

Version v1.0.3, prepared November 27, 2026. The delayed four-slot sieve and
[Ibarra's Chen lower bound](https://doi.org/10.5281/zenodo.24545780) improve the
baseline from 1.67539 to 1.67440 with the same stated density lower bound.

## Previous published versions

- aiXiv `v1.3`, [aixiv.261125.000002](https://aixiv.science/abs/aixiv.261125.000002) · [archived PDF](https://aixiv.science/pdf/aixiv.261125.000002v1.3.pdf)
- Zenodo `v1.0.2`, [version DOI](https://doi.org/10.5281/zenodo.24552165) · [all versions](https://doi.org/10.5281/zenodo.24539532)

## Files to upload

- arXiv source: `arxiv-src.zip`, containing `paper.tex` with an inline bibliography.
- aiXiv and journals: `paper.pdf` (14 pages) and `paper.tex`, with the certificate files as supplementary material where supported.
- Computational supplement: `verify_twin_upper_sieve_cert.py`, `verify_output.txt`, the `w4/` directory, and `W4-certificate-review.md`. Replay from the repository root with `python w4/verify_w4_certificate.py --recompute-baseline`.

## License

- Manuscript and PDF: CC BY 4.0.
- Python and C++ verification code: MIT.

## Comments field

14 pages. Directed integer certificates for Proposition (1-1.67440). The W4 replay uses Python 3.10+ and a C++20 compiler with 128-bit integer support. Repository: https://github.com/wellingtonthu/twin-primes-1-67539

## Declarations

- Competing interests: none.
- Data availability: the baseline and W4 code and logs are in the repository (`verify_output.txt` and `w4/verify_output.txt`).
- AI assistance: derivation and certificate implementation were produced in an AI-assisted, human-directed workflow; the analytic argument was audited and both integer certificates were independently rerun. The author takes full responsibility for the content.
