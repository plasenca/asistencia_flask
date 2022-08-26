"""
Module containing the configuration for the application.
"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    USER_ENABLE_EMAIL = False
    UPLOAD_FOLDER = "static/files"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    

class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG')
    FLASK_ENV= os.environ.get('FLASK_ENV')
    FLASK_APP= os.environ.get('FLASK_APP')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    print('DevelopmentConfig'.center(80, '-'))


class TestingConfig(Config):
    TESTING = os.environ.get('TESTING')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    print('ProductionConfig'.center(80, '-'))

config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}