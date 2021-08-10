import os


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'af532f4f0eae5f1b561af82a'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
            'postgres://', 'postgresql://') or 'postgresql:///bookswap'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
