import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://pizza_user:pizza_pass@localhost:5432/pizza_api"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False