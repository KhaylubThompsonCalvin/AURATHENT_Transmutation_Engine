import psycopg2
from psycopg2.extras import RealDictCursor

def test_connection():
    try:
        conn = psycopg2.connect(
            host="172.20.64.1",
            port=5433,
            dbname="cloeila_dev",
            user="cloeila_pub",
            password="Khalaya8!",
            cursor_factory=RealDictCursor
        )
        print("✅ Connected to PostgreSQL!")

        with conn.cursor() as cur:
            cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
            tables = cur.fetchall()
            print("📄 Public tables:")
            for t in tables:
                print(f" - {t['table_name']}")

        conn.close()
    except Exception as e:
        print("❌ Error connecting to DB:", e)

if __name__ == "__main__":
    test_connection()
