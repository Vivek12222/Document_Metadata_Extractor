import os
import pandas as pd
from tqdm import tqdm
from src.utils.parser import extract_text_docx, extract_text_image
from src.llm.extractor import extract_metadata

TEST_DIR = "data/test/"
OUTPUT_PATH = "output/test_predictions.csv"

results = []

def clean_file_name(filename):
    # Remove all known extensions from the end (including double extensions like .pdf.docx)
    for ext in [".docx", ".pdf", ".png"]:
        while filename.endswith(ext):
            filename = filename[: -len(ext)]
    return filename


for file in tqdm(os.listdir(TEST_DIR)):
    path = os.path.join(TEST_DIR, file)

    if file.endswith(".docx"):
        text = extract_text_docx(path)
    elif file.endswith(".png"):
        text = extract_text_image(path)
    else:
        continue

    metadata_json = extract_metadata(text)
    file_name = clean_file_name(file)
    
    results.append({
        "File Name": file_name,
        **metadata_json
    })

df = pd.DataFrame(results)
df.to_csv(OUTPUT_PATH, index=False)
print(f"Predictions saved to {OUTPUT_PATH}")