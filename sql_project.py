import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:Island123@localhost/sql_project')

try:
    users_df = pd.read_csv("users_data.csv")
    sessions_df = pd.read_csv("sessions_data.csv")
    purchases_df = pd.read_csv("purchases_data.csv")

    users_df.to_sql('users', engine, if_exists='replace', index=False)
    sessions_df.to_sql('sessions', engine, if_exists='replace', index=False)
    purchases_df.to_sql('purchases', engine, if_exists='replace', index=False)

    print("Dane zostały załadowane poprawnie do bazy.")
except Exception as e:
    print(f"Błąd podczas ładowania danych do bazy: {e}")
