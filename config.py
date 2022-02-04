from flask_sqlalchemy import SQLAlchemy


class Config():
    FLASK_APP = 'wsgi.py'
    FLASK_ENV =  'development'
    SECRET_KEY = 'some random and long string'

    # static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask sqlalchemy connections
    SQLAlCHEMY_DATABASE_URI = 'the connection uri'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    