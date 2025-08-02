import pandas as pd

# Load ground truth and predictions
gt = pd.read_csv("data/test.csv")            # Ground truth
pred = pd.read_csv("output/test_predictions.csv")  # Model output

# Ensure the same order and matching files
merged = pd.merge(gt, pred, on="File Name", suffixes=("_true", "_pred"))

fields = [
    "Aggrement Value",
    "Aggrement Start Date",
    "Aggrement End Date",
    "Renewal Notice (Days)",
    "Party One",
    "Party Two"
]

recall_scores = {}

for field in fields:
    true_col = field + "_true"
    pred_col = field + "_pred"

    matches = merged.apply(lambda row: str(row[true_col]).strip().lower() == str(row[pred_col]).strip().lower(), axis=1)
    true_count = matches.sum()
    total = len(matches)

    recall = true_count / total if total > 0 else 0
    recall_scores[field] = round(recall, 4)

# Print per-field recall
print("📊 Per-Field Recall Scores:")
for field, score in recall_scores.items():
    print(f"{field}: {score}")

# Optional: Macro average recall
macro_avg = sum(recall_scores.values()) / len(recall_scores)
print(f"\n⭐ Macro Average Recall: {round(macro_avg, 4)}")
