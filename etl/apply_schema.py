import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path

print("[INFO] Applying SQL schema to Neon PostgreSQL...")

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
# 3. Locate SQL schema file
# ------------------------------------------------------------
ddl_path = Path(__file__).resolve().parent.parent / "sql" / "000_schema.sql"

if not ddl_path.exists():
    raise FileNotFoundError(f"[ERROR] SQL schema file not found: {ddl_path}")

ddl_content = ddl_path.read_text(encoding="utf-8")

# ------------------------------------------------------------
# 4. Split SQL script into executable statements
# ------------------------------------------------------------
statements = [
    stmt.strip()
    for stmt in ddl_content.split(";")
    if stmt.strip()
]

# ------------------------------------------------------------
# 5. Execute schema statements
# ------------------------------------------------------------
with engine.begin() as conn:
    for stmt in statements:
        conn.execute(text(stmt))
        print("[OK] Statement executed.")

print("[INFO] Schema applied successfully.")
