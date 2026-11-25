"""Task 5 (optional): Bar chart of expected vs observed shares (10,000 draws)."""
import collections, random
import matplotlib.pyplot as plt

stake = {"Amina": 50, "Bilal": 30, "Chen": 20, "Dalia": 10}
rounds = 10000
rng = random.Random(2026)
counts = collections.Counter(rng.choices(list(stake), weights=list(stake.values()), k=rounds))
total = sum(stake.values())
names = list(stake)
exp = [stake[n] / total * 100 for n in names]
obs = [counts[n] / rounds * 100 for n in names]
x = range(len(names))
plt.bar([i - 0.2 for i in x], exp, 0.4, label="Expected %")
plt.bar([i + 0.2 for i in x], obs, 0.4, label="Observed %")
plt.xticks(list(x), names)
plt.ylabel("Selection share (%)")
plt.title("Stake-weighted selection, 10,000 draws")
plt.legend()
plt.show()
