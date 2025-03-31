import mysql.connector
import pandas as pd

DB_CONFIG = {
    'host': 'localhost',
    'user': 'arindam',
    'password': 'Arindam@81',
    'database': 'flights_db'
}

def load_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            flight_number VARCHAR(50),
            departure_airport VARCHAR(100),
            arrival_airport VARCHAR(100),
            departure_time DATETIME
        );
    """)

    df = pd.read_csv("../data/cleaned_flights.csv")
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO flights (flight_number, departure_airport, arrival_airport, departure_time)
            VALUES (%s, %s, %s, %s)
        """, (row['flight_number'], row['departure_airport'], row['arrival_airport'], row['departure_time']))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data loaded into MySQL!")

if __name__ == "__main__":
    load_data()
