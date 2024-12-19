# config.py
import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=YOURSERVER;'  # Replace with your server name
        'DATABASE=Course Registration;'  # Replace with your DB name
        "TrustServerCertificate=yes;"
        "Trusted_Connection=yes;"
    )
    return conn
