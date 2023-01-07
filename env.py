import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("16618598", "").strip()
API_HASH = os.getenv("214100c128f8cfa17c7d96bb70d3f4e2", "").strip()
BOT_TOKEN = os.getenv("5552714506:AAFi4erPQ8OR-RQGxFBirhAFatzP5I0r4g8", "").strip()
DATABASE_URL = os.getenv("mongodb+srv://Amitsaka:Amitsaka@cluster0.kmbhtsi.mongodb.net/?retryWrites=true&w=majority", "").strip()
MUST_JOIN = os.getenv("Updatesxn", "")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
