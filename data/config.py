# Created by Kamarali Anatolii at 20:11 30.10.2023 file: config.py
# проект название aiogramproject
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PGUSER = str(os.getenv("DB_USER"))
PGPASSWORD = str(os.getenv("PGPASSWORD"))
DATABASE = str(os.getenv("DATABASE"))
DBHOST = str(os.getenv("DBHOST"))
DATABASE_URL = str(os.getenv("DATABASE_URL"))

admins = [5847304479]

ip = os.getenv("ip")

aiogram_redis = {
    "host": ip,
}

redis = {"address": (ip, 6379), "encoding": "utf8"}

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
