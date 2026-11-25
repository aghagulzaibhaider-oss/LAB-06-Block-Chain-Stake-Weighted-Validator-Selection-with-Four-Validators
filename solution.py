#!/usr/bin/env python3
"""Lab 06: Stake-weighted validator selection (toy simulation, NOT a real PoS protocol).

Usage:
    python solution.py                  # 2,000 draws
    python solution.py --rounds 10000   # 10,000 draws
    python solution.py --slash          # apply toy slashing to Amina
"""
import argparse
import collections
import random

# parse_known_args lets this also run inside Colab/Jupyter without errors
parser = argparse.ArgumentParser()
parser.add_argument("--rounds", type=int, default=2000)
parser.add_argument("--slash", action="store_true")
args, _ = parser.parse_known_args()

assert 1 <= args.rounds <= 100000, "rounds must be between 1 and 100000"

# Step 1: validators and their stake (Dalia = required extension, stake 10)
stake = {"Amina": 50, "Bilal": 30, "Chen": 20, "Dalia": 10}

# Step 4: optional toy slashing - Amina loses 20 units
if args.slash:
    print("DEMO: validator Amina violated toy rules: 20 units slashed")
    stake["Amina"] -= 20

# Step 5: fixed seed -> same pseudorandom sequence every run (reproducible, not secure)
rng = random.Random(2026)

# Step 3: weighted random selection, one validator per round
choices = rng.choices(list(stake), weights=list(stake.values()), k=args.rounds)
counts = collections.Counter(choices)

# Step 2: compare expected share (stake/total) with observed share (wins/rounds)
total = sum(stake.values())
for name, amount in stake.items():
    expected = amount / total
    observed = counts[name] / args.rounds
    print(f"{name:6} stake={amount:3} expected={expected:6.1%} observed={observed:6.1%}")

assert sum(counts.values()) == args.rounds
print("EXPECTED SHARE SUM:", total, "stake units")
print("PASS: stake-weighted selection and optional penalty modeled.")
print("CAUTION: validator selection in real chains depends on protocol and many additional checks.")
