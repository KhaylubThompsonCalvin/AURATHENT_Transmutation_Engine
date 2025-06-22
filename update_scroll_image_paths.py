# update_all_scroll_paths.py

import os
import psycopg2
from psycopg2 import sql

# Config
ASSET_DIR = "/home/khaylub/CloeliaAgents/assets/01_Visual_Archives"
DB_CONFIG = {
    "host": "172.20.64.1",
    "port": 5433,
    "dbname": "cloeila_dev",
    "user": "cloeila_pub",
    "password": "Khalaya8!"
}

def main():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        updated = 0
        for filename in os.listdir(ASSET_DIR):
            if filename.endswith(".png"):
                scroll_code = filename.split("_")[0].upper()  # e.g., '007'
                image_path = os.path.join(ASSET_DIR, filename)

                cur.execute("""
                    UPDATE scroll_assets
                    SET image_path = %s
                    WHERE scroll_code = %s;
                """, (image_path, scroll_code))

                if cur.rowcount > 0:
                    print(f"✅ Updated {scroll_code}: {filename}")
                    updated += 1
                else:
                    print(f"⚠️  No match for {scroll_code} in database.")

        conn.commit()
        print(f"\n🎯 Finished. {updated} scrolls updated.")
        cur.close()
        conn.close()

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
