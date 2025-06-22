import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

# Debug: Confirm environment variables loaded
print(f"🔐 Loaded DB user: {os.getenv('DB_USER')}")
print(f"🌐 Loaded OpenAI key starts with: {os.getenv('OPENAI_API_KEY')[:8]}...")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    cursor_factory=RealDictCursor
)

# Insert scroll without tone/excerpt yet
def insert_scroll(title, subtitle, core_virtue):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO scroll_assets (title, subtitle, core_virtue, poetic_excerpt)
            VALUES (%s, %s, %s, NULL)
        """, (title, subtitle, core_virtue))
        conn.commit()
    print(f"📜 Scroll '{title}' added (awaiting calibration).")

# CLI interface
parser = argparse.ArgumentParser(description="Scroll CLI Tool (Pre-Calibration)")
parser.add_argument("--add", action="store_true", help="Add a new scroll (without tone)")
parser.add_argument("--title", type=str, help="Scroll title")
parser.add_argument("--subtitle", type=str, help="Scroll subtitle")
parser.add_argument("--virtue", type=str, help="Core virtue")

args = parser.parse_args()

if args.add:
    if args.title and args.subtitle and args.virtue:
        insert_scroll(args.title, args.subtitle, args.virtue)
    else:
        print("❌ --add requires --title, --subtitle, and --virtue")
