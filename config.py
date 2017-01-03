class BaseConfig(object):
    DEBUG = False

    # import os; os.urandom(24)
    # To set up in instance.py
    SECRET_KEY = b'isreallynotsecretatall'

    MAIL_FROM_EMAIL = "contact@example.com"

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://@/skeleton'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://@/skeleton_test'

    SERVER_NAME = 'example.com'
