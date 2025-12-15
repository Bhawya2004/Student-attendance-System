import pandas as pd

# Load baseline statistics
baseline = pd.read_csv("baseline_stats.csv", index_col=0)

# Load production data (logged predictions)
columns = [
    "age", "studytime", "failures", "absences",
    "Medu", "Fedu", "internet", "G1", "G2",
    "prediction", "probability", "timestamp"
]
prod = pd.read_csv("logs/predictions.csv", header=None, names=columns)

features = [
    "age", "studytime", "failures", "absences",
    "Medu", "Fedu", "internet", "G1", "G2"
]
prod_stats = {}

for col in features:
    prod_stats[col] = {
        "mean": prod[col].mean()
    }

prod_stats_df = pd.DataFrame(prod_stats).T
DRIFT_THRESHOLD = 2  # standard deviations

drift_report = []

for col in features:
    baseline_mean = baseline.loc[col, "mean"]
    baseline_std = baseline.loc[col, "std"]
    prod_mean = prod_stats_df.loc[col, "mean"]

    drift = abs(prod_mean - baseline_mean) > DRIFT_THRESHOLD * baseline_std

    drift_report.append({
        "feature": col,
        "baseline_mean": round(baseline_mean, 2),
        "production_mean": round(prod_mean, 2),
        "drift_detected": drift
    })

drift_df = pd.DataFrame(drift_report)

print("\nDrift Detection Report:")
print(drift_df)

drift_df.to_csv("drift_report.csv", index=False)
print("\nDrift report saved as drift_report.csv")

