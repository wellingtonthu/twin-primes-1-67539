# Proposition $(1 - 1.67539)$ on Twin Primes

**Author:** Wei Lindong (Independent Researcher, [ORCID 0009-0008-9652-2845](https://orcid.org/0009-0008-9652-2845)) · **Code license:** MIT · **Manuscript / PDF license:** CC BY 4.0

**Repository:** <https://github.com/wellingtonthu/twin-primes-1-67539> · **Citation DOI (v1.0.2):** [10.5281/zenodo.24552165](https://doi.org/10.5281/zenodo.24552165) · **Concept DOI (all versions):** [10.5281/zenodo.24539532](https://doi.org/10.5281/zenodo.24539532)

**Preprint:** [aiXiv aixiv.261125.000002](https://aixiv.science/abs/aixiv.261125.000002) · [PDF (v1.2)](https://aixiv.science/pdf/aixiv.261125.000002v1.2.pdf)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24552165.svg)](https://doi.org/10.5281/zenodo.24552165)

Unconditional, self-contained proof and pure-integer directed certificate establishing **Proposition $(1 - 1.67539)$**: for every sufficiently large $x$, more than $0.0000466\,C_2 x / (\log x)^2$ primes $p \le x$ satisfy

$$p + 2 = rq, \qquad q \text{ prime},\quad r \in \{1\} \cup \mathbb{P},\quad r \le q^{0.67539},$$

where $C_2 = 2\prod_{\ell > 2}\bigl(1 - (\ell - 1)^{-2}\bigr)$.

This improves Li and Liu's unconditional Proposition $(1 - 1.75)$ ([arXiv:2606.05224v2](https://arxiv.org/abs/2606.05224v2), Theorem 1.2) by `0.07461`.

**Revision note (`v1.0.2` + arXiv polish, 2026-11-26).** Added explicit uniform square-reserve proofs in Lemma 3.1 and §3.1, fixed the parameter selection order ($a_*$, $K_{\rm mom}$, $\kappa$) and $q>U^2$ Siegel--Walfisz tail in Proposition 4.1, corrected the two-group packing exponents, and added the citation to Chan. Subsequent pre-arXiv polish simplified Proposition 1.2 to cite Li--Liu Lemma 2.5 directly, expanded the complementary-truncation and Brun nonnegative-majorant details in Proposition 4.1, fixed the prime-power discrepancy exponent $O(x^{1-a_*/2+o(1)})$, and detailed the finite-policy density convergence in §5. The rank-one residual now uses the lower sieve function, with a uniform bound for the discrete tails. The proof also details the error from smoothing long-slot endpoints. The theorem and exact numerical bounds are unchanged.

## Summary of Results

| Method | Exponent $a$ | Bound on $r$ | Density / Status |
|---|---:|---|---|
| Li--Liu (2026, Thm. 1.2) | $1 - 1.75$ | $r \le q^{0.75}$ | $> 0.036\,C_2 x/(\log x)^2$ |
| Two-factor shortcut (§1) | $1 - 1.7078$ | $r \le q^{0.7078}$ | Elementary 1-page proof |
| Rank-three positive upper sieve | $1 - 1.6767$ | $r \le q^{0.6767}$ | Certified at $Q = 2^{80}$ |
| **Ranks three and four (Theorem 1.1)** | **$1 - 1.67539$** | **$r \le q^{0.67539}$** | **$> 0.0000466\,C_2 x/(\log x)^2$** |

**Scope distinction:** Baker and Harman (1996) proved $P^+(p+2) > p^{0.676}$ infinitely often ($p+2=rq$ with $r \le q^{0.48}$), where $r$ is a general composite integer not restricted to $\mathbb{P} \cup \{1\}$. The present theorem keeps Chen's $\Omega(p+2) \le 2$ restriction ($r = 1$ or prime). Like all one-sided linear sieve subtractions, this framework remains subject to the parity barrier and does not reach the twin prime conjecture $(1 - 1)$.

## Repository Contents

- `paper.tex` — AMS-LaTeX (`amsart`) manuscript, author fields already filled; rebuild with `build.ps1`.
- `paper.pdf` — prebuilt 12-page PDF (Latin Modern Type 1 throughout, no bitmap fonts).
- `arxiv-src.zip` — arXiv source bundle (contains only `paper.tex`; compiles standalone to the same 12 pages).
- `TwinPrime-1-minus-a-SelfContained.md` — Markdown source of the complete mathematical argument.
- `verify_twin_upper_sieve_cert.py` — Standalone pure-Python verifier using exact integer arithmetic at denominator $Q = 2^{80}$ (no floating-point operations in any certified bound, with an internal $44$-term Taylor cross-check at $s=4,\dots,12$).
- `verify_output.txt` — Recorded run of the verifier (exit code 0, with script and PDF checksums).
- `build.ps1` — Rebuilds `paper.pdf` with `pdflatex` (falls back to the local TinyTeX installation when `pdflatex` is not on `PATH`).
- `submission-metadata.md` — Copy-paste fields for arXiv/aiXiv/journal forms, including the declarations and the AI-assistance statement.
- `CITATION.cff`, `.zenodo.json`, `LICENSE` — Citation and release metadata (code MIT, manuscript CC BY 4.0).

## Reproducibility

Requires **Python 3.10+** (standard library only; no third-party dependencies):

```bash
python verify_twin_upper_sieve_cert.py
```

Expected runtime is ~3 minutes, ending with exit code `0` and printing exact numerators at $Q = 2^{80} = 1208925819614629174706176$:
- `Independent Taylor check: s=4,...,12 (both branches)`
- `U0+2u <= 3949437475976085820663535/Q`
- `G1 >= 19374509949983140898664/Q`
- `K <= 3930062966026102679764871/Q` ($\approx 3.2508719$)
- `c=12759/10000; b=67539/100000; ... margin >= 56380964408304863785/Q` ($> 0.0000466$)

A prebuilt `paper.pdf` (12 pages) is included. It was compiled locally with TinyTeX (TeX Live 2026) using three `pdflatex` passes to settle references and PDF outlines; the log has zero errors, zero overfull boxes, zero undefined references, and **no bitmap (Type 3) fonts** (Latin Modern Type 1 throughout), so the file is arXiv-ready.

To rebuild it on any standard TeX Live / Overleaf / arXiv environment:

```bash
pdflatex paper.tex
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
3. **Methodological precedent:** [Chan's Goldbach preprint](https://aixiv.science/pdf/aixiv.261111.000001v1.0.pdf), Appendix F and §8, supplies the positive prefix-sieve framework and the subtraction of excluded semiprimes. This manuscript verifies the cap changes and the progression estimate at fixed residue 2 using Pascadi's input.
4. **AI-assisted workflow note:** The mathematical derivation, integer certificate implementation, and multi-pass adversarial auditing were carried out in an AI-assisted human-directed workflow; all numerical bounds are independently verified by `verify_twin_upper_sieve_cert.py`.

## How to cite

```bibtex
@misc{wei2026twin,
  author       = {Wei, Lindong},
  title        = {A Self-Contained Proof of Proposition (1--1.67539) for the Twin Prime Problem},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v1.0.2},
  doi          = {10.5281/zenodo.24552165},
  url          = {https://doi.org/10.5281/zenodo.24552165}
}
```

Plain text: Wei Lindong, *A Self-Contained Proof of Proposition (1-1.67539) for the Twin Prime Problem*, v1.0.2, Zenodo (2026), doi:10.5281/zenodo.24552165.

To cite all versions of this project, use the concept DOI: doi:10.5281/zenodo.24539532.
