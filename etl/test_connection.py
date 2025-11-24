import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

print("[INFO] Testing database connection...")

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("[ERROR] DATABASE_URL not found in .env")

# ------------------------------------------------------------
# 2. Create database engine
# ------------------------------------------------------------
engine = create_engine(DATABASE_URL)

# ------------------------------------------------------------
# 3. Execute test query
# ------------------------------------------------------------
try:
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version();")).scalar()
        print("[OK] Connection established successfully.")
        print(f"[INFO] Server version: {version}")

except Exception as e:
    print("[ERROR] Failed to connect:")
    print(e)
