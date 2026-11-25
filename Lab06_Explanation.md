# Lab 06 - Stake-Weighted Validator Selection (Explanation)

## Purpose (short)
In Proof of Stake (PoS), validators lock up stake, and the more stake they have, the more likely they are to be chosen to propose/validate a block. This lab simulates that with a seeded weighted random draw, adds a 4th validator (Dalia), and shows how a toy "slashing" penalty lowers a validator's chances. It is a teaching model only, not real Ethereum PoS.

## Step-by-step solution with logic

**Step 1 - Stakes.** Amina 50, Bilal 30, Chen 20, Dalia 10 (the required extension). Total = 110.

**Step 2 - Expected probability = stake / total stake.**
Amina 50/110 = 45.45%, Bilal 30/110 = 27.27%, Chen 20/110 = 18.18%, Dalia 10/110 = 9.09% (sum = 100%).

**Step 3 - Simulate.** `random.Random(2026).choices(names, weights=stakes, k=rounds)` picks a validator `rounds` times, each with probability proportional to its weight. `Counter` counts wins; observed share = wins / rounds.

**Step 4 - Compare 2,000 vs 10,000 draws.** More draws reduce sampling error (law of large numbers), so observed shares get closer to expected (e.g. Amina 45.6% at 2,000, 46.5% at 10,000 vs 45.45% expected; Chen 16.2% -> 17.5% vs 18.18%). Results are still not guaranteed to match exactly.

**Step 5 - Slashing (`--slash`).** Amina loses 20 units: 50 -> 30, total = 90. New expected shares: Amina 33.33%, Bilal 33.33%, Chen 22.22%, Dalia 11.11%. Shares are always computed from the total AFTER slashing.

**Step 6 - Fixed seed.** Seed 2026 makes results reproducible (good for marking), but a seeded PRNG is not secure randomness for a real blockchain.

**Step 7 - What is missing from the toy model.** Attestations, committees, liveness, finality, real slashing evidence, adversarial behavior, deposits.

## Viva answers
1. **What do validators do beyond selection?** Check proposed blocks against protocol rules, send votes/attestations, and help reach finality.
2. **Does stake replace transaction validation?** No. Stake gives a chance to be selected, not permission to accept invalid transactions.
3. **Difference from Ethereum PoS?** Ethereum uses slots, committees, attestations, and protocol-specific finality/slashing, not a simple weighted lottery.

## Code logic summary
`argparse` reads `--rounds` and `--slash` -> `assert` validates rounds -> stake dict -> optional slash -> seeded weighted draw -> count -> print expected vs observed -> sanity asserts and PASS message.

## How to run on Colab
- Easiest: upload `Lab06_Colab.ipynb` (colab.research.google.com -> File -> Upload notebook) and Run all.
- Or upload `solution.py` and run in a cell:
  `!python solution.py`, `!python solution.py --rounds 10000`, `!python solution.py --slash`
