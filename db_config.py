import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_NAME = "northwind"
USER = "postgres"
PASSWORD = "123456"
HOST = "localhost"
PORT = "5432"

# Criando o engine de forma global para ser importado por outros módulos
engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")
Session = sessionmaker(bind=engine)

def get_psycopg_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )

def get_sqlalchemy_session():
    return Session()
