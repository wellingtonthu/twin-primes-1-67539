# Submission metadata (arXiv / aiXiv / journal forms)

Copy-paste fields for the upload forms. Values match `paper.tex` and `paper.pdf`.

## Title

A Self-Contained Proof of Proposition (1-1.67539) for the Twin Prime Problem

## Short title (running head, if asked)

Proposition (1-1.67539) for Twin Primes

## Author

- Name: Wei Lindong
- Affiliation: Independent Researcher
- Email: 744140495@qq.com

## arXiv classification

- Primary: math.NT (Number Theory)
- Cross-list: none
- MSC 2020: 11N36 (Primary); 11N05, 11P32

## Keywords

twin prime problem, Chen's theorem, weighted sieve, level of distribution, directed integer certificate

## Abstract (plain text)

For 1 <= a <= 2, Proposition (1-a) asserts that there exist infinitely many primes p such that p+2 = rq with q prime, r = 1 or prime, and r <= q^{a-1}. Li and Liu recently established Proposition (1-1.75) unconditionally. By combining Runbo Li's published lower bound pi_{1,2}(x) >= 1.2759 C_2 x / (log x)^2 with a self-contained positive upper-sieve majorant at distribution level 5/8 (derived from Pascadi's fixed-residue convolution estimate) and a directed pure-integer interval certificate at denominator 2^80, we prove Proposition (1-1.67539) unconditionally. More precisely, writing A_b(x) for the number of primes p <= x satisfying p+2 = rq with r <= q^b, we obtain A_{67539/100000}(x) > 0.0000466 C_2 x / (log x)^2 for all sufficiently large x. We also record an elementary one-page two-factor shortcut yielding Proposition (1-1.7078) and a rank-three baseline yielding Proposition (1-1.6767).

## Abstract (LaTeX, for forms that accept it)

For $1 \le a \le 2$, Proposition $(1-a)$ asserts that there exist infinitely many primes $p$ such that $p+2 = rq$ with $q$ prime, $r=1$ or prime, and $r \le q^{a-1}$. Li and Liu recently established Proposition $(1-1.75)$ unconditionally. By combining Runbo Li's published lower bound $\pi_{1,2}(x) \ge 1.2759\,C_2 x/(\log x)^2$ with a self-contained positive upper-sieve majorant at distribution level $5/8$ and a directed pure-integer interval certificate at denominator $2^{80}$, we prove Proposition $(1-1.67539)$ unconditionally. More precisely, writing $A_b(x)$ for the number of primes $p \le x$ satisfying $p+2 = rq$ with $r \le q^b$, we obtain $A_{67539/100000}(x) > 0.0000466\,C_2 x/(\log x)^2$ for all sufficiently large $x$.

## Files to upload

- arXiv: `arxiv-src.zip` (contains only `paper.tex`; no bibliography file needed, no figures).
- aiXiv / journals: `paper.pdf` (11 pages) plus the LaTeX source and `verify_twin_upper_sieve_cert.py`.

## License

- Manuscript and PDF: CC BY 4.0
- Code (`verify_twin_upper_sieve_cert.py`): MIT

## Comments field

11 pages. Includes a standalone pure-integer verifier (`verify_twin_upper_sieve_cert.py`, Python 3 standard library only) reproducing all rational bounds at denominator 2^80. Repository: https://github.com/wellingtonthu/twin-primes-1-67539 · DOI: <add Zenodo DOI>

## Declarations

- Competing interests: none.
- Data availability: all code and the recorded run log are in the repository (`verify_output.txt`).
- AI assistance: derivation and certificate implementation were produced in an AI-assisted, human-directed workflow; every analytic step was independently audited and every numerical bound is checked in exact integer arithmetic by the included verifier. The author takes full responsibility for the content.
