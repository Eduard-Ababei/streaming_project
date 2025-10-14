import psycopg2
import os
from dotenv import load_dotenv

print("🧨 Reiniciando esquema completo en Neon...")

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL").replace("postgresql+psycopg2://", "postgresql://")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("""
        DO $$
        DECLARE r RECORD;
        BEGIN
            FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
            END LOOP;
        END $$;
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Esquema público limpiado correctamente.")
except Exception as e:
    print("❌ Error durante el reseteo del esquema:")
    print(e)
