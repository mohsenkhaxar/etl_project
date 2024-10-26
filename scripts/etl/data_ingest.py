import requests
import psycopg2

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch data")

def store_data(data):
    conn = psycopg2.connect(
        dbname="gis_db",
        user="postgres",
        password="yourpassword",
        host="localhost"
    )
    cursor = conn.cursor()
    # Logic for saving data
    conn.commit()
    cursor.close()
    conn.close()
