"""Task 2: Default run, 2,000 seeded weighted draws."""
import collections, random

STAKE = {"Amina": 50, "Bilal": 30, "Chen": 20, "Dalia": 10}  # Dalia = required extension
SEED = 2026

ROUNDS = 2000
SLASH = False

stake = dict(STAKE)
if SLASH:
    print("DEMO: validator Amina violated toy rules: 20 units slashed")
    stake["Amina"] -= 20

rng = random.Random(SEED)
choices = rng.choices(list(stake), weights=list(stake.values()), k=ROUNDS)
counts = collections.Counter(choices)
total = sum(stake.values())

for name, amount in stake.items():
    print(f"{name:6} stake={amount:3} expected={amount/total:6.1%} observed={counts[name]/ROUNDS:6.1%}")

assert sum(counts.values()) == ROUNDS
print("EXPECTED SHARE SUM:", total, "stake units")
print("PASS: stake-weighted selection and optional penalty modeled.")
print("CAUTION: validator selection in real chains depends on protocol and many additional checks.")
