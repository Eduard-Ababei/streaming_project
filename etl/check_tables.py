import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

print("[INFO] Checking available tables in Neon PostgreSQL...")

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("[ERROR] DATABASE_URL not found in .env")

# ------------------------------------------------------------
# 2. Create engine and connect
# ------------------------------------------------------------
engine = create_engine(DATABASE_URL)
print("[OK] Database connection established.")

# ------------------------------------------------------------
# 3. Retrieve list of tables in 'public'
# ------------------------------------------------------------
query_tables = """
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
"""

tables = pd.read_sql(query_tables, engine)

print("[INFO] Tables found in schema 'public':")
print(tables)

# ------------------------------------------------------------
# 4. If 'movies' exists, preview data
# ------------------------------------------------------------
if "movies" in tables.values:
    print("[INFO] Previewing first rows of 'movies' table...")
    df = pd.read_sql("SELECT * FROM movies LIMIT 10;", engine)
    print(df)
else:
    print("[WARNING] Table 'movies' not found in database.")
