from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.getenv('DB_PASSWORD')
