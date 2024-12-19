
import sys
import os
import pyodbc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBConnection import dbConnection


class IDonator:
    def __init__(self):
        self.db = dbConnection()

    def display_donations(self):
        try:
            self.db.open()
            query = "SELECT * from donations"
            self.db.stmt.execute(query)
            pets = self.db.stmt.fetchall()

            if pets:
                print("Available Pets:")
                for pet in pets:
                    print(f"Name: {pet[0]}, Age: {pet[1]}, Breed: {pet[2]}")
            else:
                print("No pets available.")
        except pyodbc.Error as e:
            print(f"Error retrieving pet listings: {str(e)}")
        finally:
            self.db.close()

    def record_cash_donation(self):
        """Prompt user for donor details and record a cash donation."""
        try:
            self.db.open()
            donor_name = input("Enter donor's name: ")
            amount = float(input("Enter donation amount: "))
            donation_date = input("Enter donation date (YYYY-MM-DD): ")

            query = "INSERT INTO donations (donor_name, amount, donation_date) VALUES (?, ?, ?)"
            self.db.stmt.execute(query, (donor_name, amount, donation_date))
            self.db.conn.commit()

            print(f"Thank you, {donor_name}. Your donation of ${amount} has been recorded.")
        except pyodbc.Error as e:
            print(f"Error recording donation: {str(e)}")
        except ValueError:
            print("Invalid input for donation amount. Please enter a valid number.")
        finally:
            self.db.close()
