import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://music_user:password@localhost/music_platform')
    SQLALCHEMY_TRACK_MODIFICATIONS = False