import os

from decouple import config


class Config:
    DEBUG = config('DEBUG', default=False, cast=bool)

    DB_HOSTNAME = config('DB_HOSTNAME')
    DB_USERNAME = config('DB_USERNAME')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_PORT = config('DB_PORT')
    DB_NAME = config('DB_NAME')

    if not DEBUG:
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}"
    else:
        DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                               'database.db')
        DB_URI = 'sqlite:///{}'.format(DB_PATH)
        SQLALCHEMY_DATABASE_URI = DB_URI


class TestConfig:
    DEBUG = True
    DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                           'test_database.db')
    DB_URI = 'sqlite:///{}'.format(DB_PATH)
    SQLALCHEMY_DATABASE_URI = DB_URI
