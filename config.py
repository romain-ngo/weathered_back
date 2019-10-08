import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    # General
    TESTING = os.getenv("TESTING")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_DIALECT') + \
        os.path.join(basedir, os.getenv('DB_FILE'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        "DB_TRACK_MODIFICATIONS")

    # JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET')
