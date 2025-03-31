import pandas as pd
import requests

API_KEY = "21f063724d1de3adf3c781d0f85f6330"
URL = f"http://api.aviationstack.com/v1/flights?access_key={API_KEY}"

def fetch_data():
    response = requests.get(URL)
    data = response.json()
    df = pd.DataFrame(data['data'])
    df.to_csv('data/flights.csv', index=False)
    print("Data saved to flights.csv")

if __name__ == "__main__":
    fetch_data()
