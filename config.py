import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DB_DIALECT') + os.path.join(basedir, os.getenv('DB_FILE'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
