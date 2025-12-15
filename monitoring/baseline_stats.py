import pandas as pd

df = pd.read_csv("../data/student_ml_ready.csv")

features = [
    "age", "studytime", "failures", "absences",
    "Medu", "Fedu", "internet", "G1", "G2"
]

baseline = {}

for col in features:
    baseline[col] = {
        "mean": df[col].mean(),
        "std": df[col].std()
    }

baseline_df = pd.DataFrame(baseline).T
baseline_df.to_csv("baseline_stats.csv")

print("Baseline statistics saved")
