# config.py
POSTGRESQL = "postgresql+psycopg2://postgres:tor@localhost:5432/blogposts-db"

class Config:
    DEBUG = True
    SECRET_KEY = "dev"
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    CKEDITOR_PKG_TYPE="full"
    

