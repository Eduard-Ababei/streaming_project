import psycopg2, ssl

print("🔍 Intentando conexión directa a Neon (sin DNS)...")

# Datos reales de tu conexión
user = "neondb_owner"
password = "npg_lIsAn4uah9MT"
dbname = "neondb"
host = "ep-old-lake-ab7aayzq-pooler.eu-west-2.aws.neon.tech"
port = 5432

# Configuración SSL (segura)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

try:
    conn = psycopg2.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        dbname=dbname,
        sslmode="require",
        target_session_attrs="read-write"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("✅ Conectado correctamente a Neon.")
    print("Versión del servidor:", version[0])
    cur.close()
    conn.close()
except Exception as e:
    print("❌ Error de conexión:")
    print(e)
