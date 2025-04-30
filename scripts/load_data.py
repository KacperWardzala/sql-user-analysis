import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

users = pd.read_csv('data/users_data.csv')
sessions = pd.read_csv('data/sessions_data.csv')
purchases = pd.read_csv('data/purchases_data.csv')

users.to_sql('users', engine, if_exists='replace', index=False)
sessions.to_sql('sessions', engine, if_exists='replace', index=False)
purchases.to_sql('purchases', engine, if_exists='replace', index=False)

print("Data loaded successfully.")
