import psycopg2
import ssl

print("🔍 Verificando tablas reales en Neon (conexión directa SSL)...")

try:
    conn = psycopg2.connect(
        user="neondb_owner",
        password="npg_lIsAn4uah9MT",
        host="ep-old-lake-ab7aayzq-pooler.eu-west-2.aws.neon.tech",
        port=5432,
        dbname="neondb",
        sslmode="require"
    )

    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)
    tables = cur.fetchall()

    if not tables:
        print("⚠️  No hay tablas encontradas en la base de datos.")
    else:
        print("✅ Tablas encontradas:")
        for t in tables:
            print(" -", t[0])

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error verificando las tablas:")
    print(e)
