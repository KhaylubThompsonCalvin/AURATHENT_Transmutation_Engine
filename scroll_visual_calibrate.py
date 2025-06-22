import os
import base64
import argparse
import psycopg2
from psycopg2.extras import RealDictCursor
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# PostgreSQL connection
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    cursor_factory=RealDictCursor
)

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def analyze_scroll_with_image(title, virtue, image_path):
    if not os.path.isfile(image_path):
        return "❌ Image file not found.", None, None

    print(f"🖼️ Sending image: {image_path}...")

    base64_image = encode_image_to_base64(image_path)
    image_data_url = f"data:image/png;base64,{base64_image}"

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an ancient scribe trained in symbolic decoding. Analyze the scroll's image and describe its mythic, philosophical, or virtue-based meaning."
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"This is the scroll titled '{title}', aligned with the virtue of '{virtue}'. Analyze its symbolic meaning."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_data_url
                        }
                    }
                ]
            }
        ]
    )

    result = response.choices[0].message.content.strip()
    return result, image_path, title

def calibrate_scroll(scroll_code):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM scroll_assets WHERE scroll_code = %s", (scroll_code,))
        scroll = cur.fetchone()

        if not scroll:
            print(f"❌ No scroll found with scroll_code = {scroll_code}")
            return

        title = scroll["title"]
        virtue = scroll["core_virtue"]
        image_path = scroll["image_path"]

        output, image_url, title = analyze_scroll_with_image(title, virtue, image_path)

        print("\n📜 Symbolic Analysis:")
        print(f"Scroll: {title}")
        print(f"Image Path: {image_url}")
        print(f"\n🧠 Interpretation:\n{output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scroll Visual Calibration Tool")
    parser.add_argument("--id", type=str, required=True, help="Scroll code (e.g., 055)")
    args = parser.parse_args()

    calibrate_scroll(args.id)
