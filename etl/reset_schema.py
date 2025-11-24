import psycopg2
import os
from dotenv import load_dotenv

print("[INFO] Resetting public schema in Neon PostgreSQL...")

# ------------------------------------------------------------
# 1. Load environment variables
# ------------------------------------------------------------
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("[ERROR] DATABASE_URL not found in .env")

# psycopg2 requires postgresql:// format
DATABASE_URL = DATABASE_URL.replace("postgresql+psycopg2://", "postgresql://")

# ------------------------------------------------------------
# 2. Execute schema reset
# ------------------------------------------------------------
try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    reset_sql = """
    DO $$
    DECLARE r RECORD;
    BEGIN
        FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
            EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
        END LOOP;
    END $$;
    """

    cur.execute(reset_sql)
    conn.commit()

    cur.close()
    conn.close()

    print("[OK] Public schema cleared successfully.")

except Exception as e:
    print("[ERROR] Failed to reset schema:")
    print(e)
