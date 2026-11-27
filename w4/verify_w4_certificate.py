"""Replay the W4 integer certificate and check the b=0.67440 margin."""

import argparse
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import re
import runpy
import subprocess
import sys
from tempfile import TemporaryDirectory

from make_table import BASELINE, TABLE_SCALE, write_table

BOX_LIMIT = 8_500_000
EXPECTED_EVALUATIONS = 8_500_001
EXPECTED_DELTA = (185080395990360007633, 311314004869422725676)
BASE_U0_NUM = 3949437475976085820663535
BASE_GAIN_NUM = 19374509949983140898664
EXPECTED_GAIN_NUM = 19598258419400386998038
EXPECTED_K_NUM = 3929839217556685433665497
EXPECTED_MARGIN_NUM = 61483810070100487491


def check(condition, message):
    if not condition:
        raise ValueError(message)


def replay(compiler, verifier):
    source = Path(__file__).with_name("ordered_boxes.cpp").resolve()
    with TemporaryDirectory(prefix="twin-w4-") as work:
        directory = Path(work)
        table = directory / "sieve_table.txt"
        write_table(table, verifier)
        print(f"sieve_table_sha256: {sha256(table.read_bytes()).hexdigest()}", flush=True)
        executable = directory / "ordered_boxes.exe"
        subprocess.run(
            [compiler, "-std=c++20", "-O3", str(source), "-o", str(executable)],
            cwd=work,
            check=True,
        )
        output = subprocess.check_output(
            [str(executable), str(BOX_LIMIT)], cwd=work, text=True, encoding="ascii"
        )
    print(output, end="", flush=True)
    count, low, high, denominator = map(
        int, output.splitlines()[-1].replace(" / ", " ").split()
    )
    check(count == EXPECTED_EVALUATIONS, "Unexpected W4 evaluation count")
    check((low, high) == EXPECTED_DELTA, "W4 interval differs from the reviewed result")
    check(denominator == TABLE_SCALE**2, "Unexpected W4 interval denominator")
    return Fraction(low, denominator)


def verify_baseline(q):
    output = subprocess.check_output(
        [sys.executable, str(BASELINE)],
        cwd=BASELINE.parent,
        text=True,
        encoding="ascii",
    )
    match = re.search(
        rf"U0\+2u <= (\d+)/{q}; G1 >= (\d+)/{q}; K <= (\d+)/{q}", output
    )
    expected = (BASE_U0_NUM, BASE_GAIN_NUM, BASE_U0_NUM - BASE_GAIN_NUM)
    check(match and tuple(map(int, match.groups())) == expected,
          "Recomputed baseline differs from the published certificate")
    print(output, end="")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cxx", default="g++", help="C++20 compiler with __int128")
    parser.add_argument("--recompute-baseline", action="store_true",
                        help="also rerun the unchanged original verifier")
    args = parser.parse_args()
    verifier = runpy.run_path(str(BASELINE))
    q = verifier["Q"]
    check(q == 2**80, "Unexpected baseline denominator")
    print(f"baseline_script_sha256: {sha256(BASELINE.read_bytes()).hexdigest()}")
    delta_lo = replay(args.cxx, verifier)
    gain_num = BASE_GAIN_NUM + (delta_lo*q).__floor__()
    k_num = BASE_U0_NUM - gain_num
    check(gain_num == EXPECTED_GAIN_NUM, "Unexpected G1_new numerator")
    check(k_num == EXPECTED_K_NUM, "Unexpected K_new numerator")
    b = Fraction(3372, 5000)
    c = Fraction(6403, 5000)
    log_hi = verifier["logarithm"](1/b)[1]
    margin_num = ((c - Fraction(k_num, q)*log_hi)*q).__floor__()
    check(margin_num == EXPECTED_MARGIN_NUM, "Unexpected margin numerator")
    check(Fraction(margin_num, q) > Fraction(466, 10**7),
          "The certified margin does not exceed 0.0000466")
    print(f"G1_new >= {gain_num}/{q}")
    print(f"K_new <= {k_num}/{q}")
    print(f"c={c}; b={b}; margin >= {margin_num}/{q} > 0.0000466", flush=True)
    if args.recompute_baseline:
        print("Recomputing the unchanged baseline", flush=True)
        verify_baseline(q)
    else:
        print("Baseline inputs taken from the published integer certificate")
    print("W4 certificate verified")


if __name__ == "__main__":
    main()
