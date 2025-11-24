import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from pathlib import Path

print("[INFO] Loading cleaned dataset into Neon PostgreSQL...")

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("[ERROR] DATABASE_URL not found in .env")

engine = create_engine(DATABASE_URL)

# ------------------------------------------------------------
# 2. Locate cleaned CSV file
# ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "clean" / "movies_clean.csv"

if not CSV_PATH.exists():
    raise FileNotFoundError(f"[ERROR] Cleaned dataset not found: {CSV_PATH}")

df = pd.read_csv(CSV_PATH)
print(f"[INFO] Clean dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# ------------------------------------------------------------
# 3. Load data into database
# ------------------------------------------------------------
with engine.begin() as conn:
    # Remove existing table if present
    conn.execute(text("DROP TABLE IF EXISTS movies CASCADE"))

    # Load into database
    df.to_sql("movies", con=conn, if_exists="replace", index=False)

print("[OK] Table 'movies' created and data loaded successfully.")
