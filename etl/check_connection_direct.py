import psycopg2
import os
from dotenv import load_dotenv

print("[INFO] Testing direct connection to Neon PostgreSQL...")

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("[ERROR] DATABASE_URL not found in .env")

# psycopg2 requires plain postgresql:// format
DATABASE_URL = DATABASE_URL.replace("postgresql+psycopg2://", "postgresql://")

# ------------------------------------------------------------
# 2. Attempt connection
# ------------------------------------------------------------
try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute("SELECT version();")
    version = cur.fetchone()

    print("[OK] Connection successful.")
    print(f"[INFO] PostgreSQL version: {version[0]}")

    cur.close()
    conn.close()

except Exception as e:
    print("[ERROR] Connection failed:")
    print(e)
