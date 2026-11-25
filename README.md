# Lab 06 - Stake-Weighted Validator Selection with Four Validators

Course: Introduction to Blockchain (Linux Lab)

## Purpose
This lab simulates a simplified Proof of Stake (PoS) validator selection. Validators with more stake are more likely to be chosen. A seeded random generator performs weighted draws among four validators (Amina, Bilal, Chen, Dalia), and an optional toy "slashing" penalty reduces one validator's stake to show how incentives change selection chances.

This is an educational model only. It is NOT a real PoS protocol (no attestations, finality, committees, or secure randomness).

## Files
| File | Description |
|------|-------------|
| `solution.py` | Main Python script |
| `Lab06_Colab.ipynb` | Google Colab notebook with all tasks as separate cells |
| `README.md` | This file |
| `Viva_Answers.md` | Viva questions and model answers |

## Requirements
- Python 3.8+ (standard library only: `argparse`, `collections`, `random`)
- Optional: `matplotlib` (only for the chart cell in the notebook; preinstalled on Colab)

## How to Run

### Linux / local
```bash
python3 solution.py                  # 2,000 draws (default)
python3 solution.py --rounds 10000   # 10,000 draws
python3 solution.py --slash          # slash Amina by 20 units
```

### Google Colab
1. Go to colab.research.google.com, then File -> Upload notebook, and choose `Lab06_Colab.ipynb`.
2. Run all cells from top to bottom.

Or upload `solution.py` to Colab and run:
```
!python solution.py
!python solution.py --rounds 10000
!python solution.py --slash
```

## Arguments
| Argument | Default | Meaning |
|----------|---------|---------|
| `--rounds N` | 2000 | Number of random draws (1 to 100000) |
| `--slash` | off | Reduce Amina's stake from 50 to 30 |

## How It Works
1. Define stakes: Amina 50, Bilal 30, Chen 20, Dalia 10 (total 110).
2. If `--slash` is given, Amina loses 20 units (total becomes 90).
3. Create `random.Random(2026)` so results are repeatable.
4. Use `rng.choices(names, weights=stakes, k=rounds)` to pick a validator each round.
5. Count wins with `collections.Counter`.
6. Print expected share (stake / total) against observed share (wins / rounds).
7. Run sanity assertions and print a PASS message.

## Expected Probabilities
| Validator | Normal | After `--slash` |
|-----------|--------|-----------------|
| Amina | 45.45% (50/110) | 33.33% (30/90) |
| Bilal | 27.27% (30/110) | 33.33% (30/90) |
| Chen | 18.18% (20/110) | 22.22% (20/90) |
| Dalia | 9.09% (10/110) | 11.11% (10/90) |

## Sample Output (default run)
```
Amina  stake= 50 expected= 45.5% observed= 45.6%
Bilal  stake= 30 expected= 27.3% observed= 28.4%
Chen   stake= 20 expected= 18.2% observed= 16.2%
Dalia  stake= 10 expected=  9.1% observed=  9.8%
EXPECTED SHARE SUM: 110 stake units
PASS: stake-weighted selection and optional penalty modeled.
CAUTION: validator selection in real chains depends on protocol and many additional checks.
```

## Notes
- Larger `--rounds` values give observed shares closer to expected, but never guaranteed to match exactly.
- Expected shares are always calculated from the total stake after any slashing.
- The fixed seed is useful for marking but is not secure randomness for a real blockchain.
- Results are not predictions of financial returns.

## Submission Checklist
- Command transcript (screenshots of all three runs)
- Code (`solution.py`)
- Result table or chart
- Three viva answers (`Viva_Answers.md`)
