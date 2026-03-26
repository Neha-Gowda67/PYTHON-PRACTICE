import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load dataset
df = pd.read_csv("beml_stock_data.csv")

# Clean price column (if needed)
df['Price'] = df['Price'].astype(str).str.replace(',', '').astype(float)

# -----------------------------
# 📊 BASIC STATISTICS
# -----------------------------
mean_price = df['Price'].mean()
median_price = df['Price'].median()
std_price = df['Price'].std()

print("Mean:", mean_price)
print("Median:", median_price)
print("Standard Deviation:", std_price)

# -----------------------------
# 📈 Z-TEST
# -----------------------------
sample = df['Price'].tail(30)
population = df['Price']

sample_mean = np.mean(sample)
population_mean = np.mean(population)
population_std = np.std(population)
n = len(sample)

z_score = (sample_mean - population_mean) / (population_std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

print("\nZ-score:", round(z_score, 4))
print("P-value:", round(p_value, 4))

if p_value < 0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")

# -----------------------------
# 📉 PRICE OVER TIME GRAPH
# -----------------------------
plt.figure()
plt.plot(df['Price'])
plt.title("Stock Price Over Time")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid()
plt.show()

# -----------------------------
# 📊 ROLLING MEAN
# -----------------------------
df['Rolling Mean'] = df['Price'].rolling(window=12).mean()

plt.figure()
plt.plot(df['Price'], label="Original")
plt.plot(df['Rolling Mean'], label="Rolling Mean")
plt.legend()
plt.title("Rolling Mean")
plt.show()

# -----------------------------
# 📉 VOLATILITY
# -----------------------------
df['Change %'] = df['Price'].pct_change() * 100

plt.figure()
plt.plot(df['Change %'])
plt.title("Volatility (Daily % Change)")
plt.show()
