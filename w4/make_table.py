"""Generate the outward-rounded sieve value and slope table for W4."""

import argparse
from pathlib import Path
import runpy

BASELINE = Path(__file__).resolve().parents[1] / "verify_twin_upper_sieve_cert.py"
TABLE_SCALE = 10**12


def write_table(destination, verifier):
    at, at_slope = verifier["at"], verifier["at_slope"]
    q, n = verifier["Q"], verifier["n"]
    if n != 4096:
        raise ValueError("The W4 evaluator expects a 1/4096 sieve mesh")
    at.__globals__["TAB"] = verifier["sieve_table"]()
    with destination.open("w", encoding="ascii", newline="\n") as table:
        for i in range(n, 12*n + 1):
            value_lo, value_hi = at(0, i, n)
            slope_lo, slope_hi = at_slope(0, i, n, value_lo, value_hi)
            print(
                value_lo*TABLE_SCALE//q,
                -(-value_hi*TABLE_SCALE//q),
                slope_lo*TABLE_SCALE//q,
                -(-slope_hi*TABLE_SCALE//q),
                file=table,
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="path to the generated table")
    args = parser.parse_args()
    write_table(args.output, runpy.run_path(str(BASELINE)))
