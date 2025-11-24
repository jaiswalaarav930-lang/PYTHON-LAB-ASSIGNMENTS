import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("weather_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("Head:")
print(df.head())
print("\nBasic stats:")
print(df.describe())

# 2. Daily temperature line plot
plt.figure()
plt.plot(df["Date"], df["Temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Daily Temperature Trend")
plt.tight_layout()
plt.savefig("temp_trend.png")
plt.close()

# 3. Monthly rainfall bar chart
df_month = df.set_index("Date").resample("M").sum(numeric_only=True)

plt.figure()
plt.bar(df_month.index.strftime("%Y-%m"), df_month["Rainfall"])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Total Rainfall")
plt.title("Monthly Rainfall")
plt.tight_layout()
plt.savefig("monthly_rain.png")
plt.close()

# 4. Humidity vs temperature scatter
plt.figure()
plt.scatter(df["Temperature"], df["Humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.tight_layout()
plt.savefig("humidity_vs_temp.png")
plt.close()

print("\nPlots saved as:")
print("  temp_trend.png")
print("  monthly_rain.png")
print("  humidity_vs_temp.png")
