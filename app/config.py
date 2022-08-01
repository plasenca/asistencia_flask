"""
Module containing the configuration for the application.
"""
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG')
    FLASK_ENV= os.environ.get('FLASK_ENV')
    FLASK_APP= os.environ.get('FLASK_APP')
    print('DevelopmentConfig'.center(80, '-'))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


class TestingConfig(Config):
    TESTING = os.environ.get('TESTING')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass

config = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DevelopmentConfig
}