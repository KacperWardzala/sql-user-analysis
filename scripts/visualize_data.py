import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

users = pd.read_sql("SELECT * FROM users", engine)
sessions = pd.read_sql("SELECT * FROM sessions", engine)
purchases = pd.read_sql("SELECT * FROM purchases", engine)

os.makedirs("plots", exist_ok=True)

sessions_count = sessions.groupby("user_id").size().reset_index(name="session_count")
plt.figure(figsize=(12, 6))
plt.bar(sessions_count["user_id"].astype(str), sessions_count["session_count"], width=0.6)
plt.xlabel("User ID", fontsize=10)
plt.ylabel("Session Count", fontsize=10)
plt.title("Number of Sessions per User", fontsize=12)
plt.xticks(rotation=90, fontsize=8, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.tight_layout(pad=5.0)
plt.savefig("plots/sessions_per_user.png")
plt.close()

avg_purchase = purchases.groupby("user_id")["amount"].mean().reset_index()
plt.figure(figsize=(12, 6))
plt.bar(avg_purchase["user_id"].astype(str), avg_purchase["amount"], width=0.6)
plt.xlabel("User ID", fontsize=10)
plt.ylabel("Average Purchase Amount", fontsize=10)
plt.title("Average Purchase Amount per User", fontsize=12)
plt.xticks(rotation=90, fontsize=8, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.tight_layout(pad=5.0)
plt.savefig("plots/avg_purchase_per_user.png")
plt.close()

purchases["purchase_date"] = pd.to_datetime(purchases["purchase_date"])
daily_purchases = purchases.groupby(purchases["purchase_date"].dt.date).size()
plt.figure(figsize=(12, 6))
daily_purchases.plot(kind="bar", width=0.6)
plt.xlabel("Date", fontsize=10)
plt.ylabel("Number of Purchases", fontsize=10)
plt.title("Number of Purchases per Day", fontsize=12)
plt.xticks(rotation=90, fontsize=8, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.tight_layout(pad=5.0)
plt.savefig("plots/purchases_per_day.png")
plt.close()

if "country" in users.columns:
    country_counts = users["country"].value_counts()
    plt.figure(figsize=(12, 6))
    country_counts.plot(kind="bar", width=0.6)
    plt.xlabel("Country", fontsize=10)
    plt.ylabel("Number of Users", fontsize=10)
    plt.title("User Distribution by Country", fontsize=12)
    plt.xticks(rotation=90, fontsize=8, ha='right')
    plt.subplots_adjust(bottom=0.2)
    plt.tight_layout(pad=5.0)
    plt.savefig("plots/users_by_country.png")
    plt.close()
