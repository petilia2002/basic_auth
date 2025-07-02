import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    HOST = os.getenv("HOST", "localhost")
    PORT = os.getenv("PORT", 5000)
    DEBUG = os.getenv("DEBUG", True)
    SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")
