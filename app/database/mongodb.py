# Administración de conexión con MongoDB
from pymongo import MongoClient
from app.config.settings import Config

def get_db():
    client = MongoClient(Config.MONGO_URI)
    return client.get_database()
