import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ils_x_sweep.csv")

plt.figure(figsize=(10,6))
plt.plot(df["X"], df["avg"], marker='o', label="Average")
plt.plot(df["X"], df["min"], marker='o', label="Minimum")
plt.plot(df["X"], df["max"], marker='o', label="Maximum")

plt.xlabel("Perturbation size X")
plt.ylabel("Objective value")
plt.title("ILS Performance vs Perturbation Strength X")
plt.legend()
plt.grid(True)
plt.show()
