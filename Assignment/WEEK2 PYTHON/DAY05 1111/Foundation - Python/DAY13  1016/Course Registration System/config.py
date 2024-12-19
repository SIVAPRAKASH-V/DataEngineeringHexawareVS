# config.py
import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Server};'
        'SERVER=YOURSERVERNAME;'  
        'DATABASE=Course Registration;'  
        "TrustServerCertificate=yes;"
        "Trusted_Connection=yes;"
    )
    return conn
