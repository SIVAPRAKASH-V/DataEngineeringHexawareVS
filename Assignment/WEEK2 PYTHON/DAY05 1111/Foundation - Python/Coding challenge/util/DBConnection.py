import sys
import os
import pyodbc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBPropertyUtil import DBPropertyUtil

class dbConnection:
    def __init__(self):
        self.conn = None

    def open(self):
        try:
            db_details = DBPropertyUtil.get_property_string()
            connection_string = (f"Driver={{{db_details[0]}}};"
                                 f"Server={db_details[1]};"
                                 f"Database={db_details[2]};"
                                 f"TrustServerCertificate={db_details[3]};"
                                 f"Trusted_Connection={db_details[4]};")
            self.conn = pyodbc.connect(connection_string)
            if self.conn:
                print("--Database Is Connected--")
            self.stmt=self.conn.cursor()
            return "Connected Database"
        except Exception as e:
            print(f"Error while connecting to the DB: {e}")

    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(f"Error while closing the DB connection: {e}")

            
data=dbConnection()
data.open()
data.close()
