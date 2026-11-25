# Proposition $(1 - 1.67539)$ on Twin Primes

**Author:** Wei Lindong (Independent Researcher) · **Code license:** MIT · **Manuscript / PDF license:** CC BY 4.0

**Repository:** <https://github.com/wellingtonthu/twin-primes-1-67539> · **Citation DOI (v1.0.0):** [10.5281/zenodo.24539533](https://doi.org/10.5281/zenodo.24539533) · **Concept DOI (all versions):** [10.5281/zenodo.24539532](https://doi.org/10.5281/zenodo.24539532)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24539533.svg)](https://doi.org/10.5281/zenodo.24539533)

Unconditional, self-contained proof and pure-integer directed certificate establishing **Proposition $(1 - 1.67539)$**: for every sufficiently large $x$, more than $0.0000466\,C_2 x / (\log x)^2$ primes $p \le x$ satisfy

$$p + 2 = rq, \qquad q \text{ prime},\quad r \in \{1\} \cup \mathbb{P},\quad r \le q^{0.67539},$$

where $C_2 = 2\prod_{\ell > 2}\bigl(1 - (\ell - 1)^{-2}\bigr)$.

This improves Li and Liu's unconditional Proposition $(1 - 1.75)$ ([arXiv:2606.05224v2](https://arxiv.org/abs/2606.05224v2), Theorem 1.2) by `0.07461`.

## Summary of Results

| Method | Exponent $a$ | Bound on $r$ | Density / Status |
|---|---:|---|---|
| Li--Liu (2026, Thm. 1.2) | $1 - 1.75$ | $r \le q^{0.75}$ | $> 0.036\,C_2 x/(\log x)^2$ |
| Two-factor shortcut (§1) | $1 - 1.7078$ | $r \le q^{0.7078}$ | Elementary 1-page proof |
| Rank-three positive upper sieve | $1 - 1.6767$ | $r \le q^{0.6767}$ | Certified at $Q = 2^{80}$ |
| **Ranks three and four (Theorem 1.1)** | **$1 - 1.67539$** | **$r \le q^{0.67539}$** | **$> 0.0000466\,C_2 x/(\log x)^2$** |

**Scope distinction:** Baker and Harman (1996) proved $P^+(p+2) > p^{0.676}$ infinitely often ($p+2=rq$ with $r \le q^{0.48}$), where $r$ is a general composite integer not restricted to $\mathbb{P} \cup \{1\}$. The present theorem keeps Chen's $\Omega(p+2) \le 2$ restriction ($r = 1$ or prime). Like all one-sided linear sieve subtractions, this framework remains subject to the parity barrier and does not reach the twin prime conjecture $(1 - 1)$.

## Repository Contents

- `paper.tex` — Publication-ready AMS-LaTeX manuscript (`amsart`). Fill in author/affiliation fields before arXiv or journal submission.
- `verify_twin_upper_sieve_cert.py` — Standalone pure-Python verifier using exact integer arithmetic at denominator $Q = 2^{80}$ (no floating-point operations in any certified bound, with an internal $44$-term Taylor cross-check at $s=4,\dots,12$).
- `TwinPrime-1-minus-a-SelfContained.md` — Markdown source of the complete mathematical argument.
- `知乎文章草稿.md` — Chinese exposition and video-script draft summarizing the background, proof mechanism, and verification workflow.
- `CITATION.cff`, `.zenodo.json`, `LICENSE` — Citation and release metadata for GitHub + Zenodo DOI minting.

## Reproducibility

Requires **Python 3.10+** (standard library only; no third-party dependencies):

```bash
python verify_twin_upper_sieve_cert.py
```

Expected runtime is ~3 minutes, ending with exit code `0` and printing exact numerators at $Q = 2^{80} = 1208925819614629174706176$:
- `Independent Taylor check: s=4,...,12 (both branches)`
- `U0+2u <= 3949437475976085820663535/Q`
- `G1 >= 19374509949983140898664/Q`
- `K <= 3930062966026102679764871/Q` ($\approx 3.2508717$)
- `c=12759/10000; b=67539/100000; ... margin >= 56380964408304863785/Q` ($> 0.0000466$)

A prebuilt `paper.pdf` (11 pages) is included. It was compiled locally with TinyTeX (TeX Live 2026) using `pdflatex` twice; the log has zero errors, zero overfull boxes, zero undefined references, and **no bitmap (Type 3) fonts** (Latin Modern Type 1 throughout), so the file is arXiv-ready.

To rebuild it on any standard TeX Live / Overleaf / arXiv environment:

```bash
pdflatex paper.tex
pdflatex paper.tex
```

Local Windows toolchain used here (no admin rights needed):

```powershell
# portable TinyTeX, single self-extracting archive
# https://github.com/rstudio/tinytex-releases/releases/download/v2026.11/TinyTeX-1-windows-v2026.11.exe
& TinyTeX-1-windows-v2026.11.exe -y -o"$env:LOCALAPPDATA\TinyTeX"
$env:PATH = "$env:LOCALAPPDATA\TinyTeX\TinyTeX\bin\windows;$env:PATH"
pdflatex paper.tex
```

## External Inputs & Transparency

1. **Published Chen lower bound:** Runbo Li, *Mathematical Reports* **28** (2026), no. 1--2, 39--61 ([arXiv:2405.05727v4](https://arxiv.org/abs/2405.05727v4), Theorem 1.3): $\pi_{1,2}(x) \ge 1.2759\,C_2 x / (\log x)^2$.
2. **Distribution level $5/8$:** Alexandru Pascadi, *On the exponents of distribution of primes and smooth numbers* ([arXiv:2505.00653v1](https://arxiv.org/abs/2505.00653v1), Proposition 4.4 / eq. (4.15)).
3. **AI-assisted workflow note:** The mathematical derivation, integer certificate implementation, and multi-pass adversarial auditing were carried out in an AI-assisted human-directed workflow; all numerical bounds are independently verified by `verify_twin_upper_sieve_cert.py`.
