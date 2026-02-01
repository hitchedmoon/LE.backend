import os
from dotenv import load_dotenv

load_dotenv()

class Config:  # <--- Make sure this is "Config" with a capital C
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')