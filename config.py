import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secure_string"

    MONGODB_SETTINGS = {'db': 'optimizer_db'}
    