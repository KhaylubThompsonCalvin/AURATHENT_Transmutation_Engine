import os
import psycopg2
from psycopg2.extras import RealDictCursor
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

# Set up LangChain/OpenAI
llm = ChatOpenAI(temperature=0.6, openai_api_key=os.getenv("OPENAI_API_KEY"))

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    cursor_factory=RealDictCursor
)

# Define LangChain prompt
calibration_prompt = PromptTemplate(
    input_variables=["title", "virtue"],
    template="""
You are the AI Voice of the Vault. A sacred scroll has been unearthed.

Title: "{title}"
Core Virtue: "{virtue}"

Based on the title and virtue, generate:
1. A poetic excerpt (1–2 mythic lines, sacred tone)
2. An emotional theme word (e.g. Hope, Vengeance, Transcendence)
3. A tone signature (single phrase capturing delivery style, e.g. "haunting grace", "resolute fury")

Respond in the following format:

[Poetic Excerpt]
[Emotional Theme]
[Tone Signature]
"""
)

def calibrate_scroll(scroll_id):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM scroll_assets WHERE id = %s", (scroll_id,))
        row = cur.fetchone()

        if not row:
            print(f"❌ No scroll found with ID {scroll_id}")
            return

        title = row["title"]
        virtue = row["core_virtue"]

        # Generate response
        prompt = calibration_prompt.format(title=title, virtue=virtue)
        response = llm.predict(prompt)

        try:
            poetic, emotion, tone = [line.strip() for line in response.strip().split("\n")]
        except:
            print("⚠️ Unexpected response format. Output:")
            print(response)
            return

        # Update DB
        cur.execute("""
            UPDATE scroll_assets
            SET poetic_excerpt = %s,
                emotional_theme = %s,
                tone_signature = %s
            WHERE id = %s
        """, (poetic, emotion, tone, scroll_id))
        conn.commit()

        print("✅ Scroll calibrated:")
        print(f"📜 {poetic}")
        print(f"💧 Theme: {emotion}")
        print(f"🔊 Tone: {tone}")

# CLI Interface
parser = argparse.ArgumentParser(description="Calibrate a Scroll (AI Tone Generator)")
parser.add_argument("--id", type=int, required=True, help="ID of scroll to calibrate")

args = parser.parse_args()

calibrate_scroll(args.id)
