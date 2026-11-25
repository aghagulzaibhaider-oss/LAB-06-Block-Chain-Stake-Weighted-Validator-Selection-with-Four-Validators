"""Task 1: Predict expected selection probabilities by hand (stake / total)."""
stake = {"Amina": 50, "Bilal": 30, "Chen": 20, "Dalia": 10}
total = sum(stake.values())
print("Total stake =", " + ".join(map(str, stake.values())), "=", total)
for name, amount in stake.items():
    print(f"{name:6} {amount}/{total} = {amount/total:.2%}")
print("Sum of probabilities:", round(sum(a / total for a in stake.values()), 6))
