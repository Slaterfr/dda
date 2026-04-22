from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    GEKO_KEY = os.getenv('GEKO-API-KEY')
    DATABASE_URI = os.getenv('DATABASE_URI')