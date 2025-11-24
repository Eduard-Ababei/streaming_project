import pandas as pd
from pathlib import Path

print("[INFO] Starting dataset cleaning...")

# ------------------------------------------------------------
# 1. Determine project paths
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

RAW_PATH = DATA_DIR / "raw" / "movies_raw.csv"
CLEAN_PATH = DATA_DIR /"clean" / "movies_clean.csv"

# ------------------------------------------------------------
# 2. Load dataset
# ------------------------------------------------------------
if not RAW_PATH.exists():
    raise FileNotFoundError(f"[ERROR] Raw dataset not found: {RAW_PATH}")

df = pd.read_csv(RAW_PATH)
print(f"[INFO] Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ------------------------------------------------------------
# 3. Clean dataset
# ------------------------------------------------------------
required_columns = ["title", "release_year", "listed_in", "rating", "country"]

missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    raise ValueError(f"[ERROR] Missing required columns: {missing_cols}")

df = df[required_columns].dropna()

print(f"[INFO] Cleaning complete. Final rows: {df.shape[0]}")

# ------------------------------------------------------------
# 4. Save cleaned dataset
# ------------------------------------------------------------
df.to_csv(CLEAN_PATH, index=False)
print(f"[OK] Clean dataset saved to: {CLEAN_PATH}")
