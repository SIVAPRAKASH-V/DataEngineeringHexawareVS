import sys
import os
import pyodbc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBConnection import dbConnection

class IParticipants:
    def __init__(self):
        self.db = dbConnection()
    def manage_adoption_events(self):
        """Retrieve adoption events and allow user registration."""
        try:
            self.db.open()
            # Display available adoption events
            query = "SELECT event_id, event_name, event_date FROM adoption_events"
            self.db.stmt.execute(query)
            events = self.db.stmt.fetchall()

            if events:
                print("Upcoming Adoption Events:")
                for event in events:
                    print(f"ID: {event[0]}, Name: {event[1]}, Date: {event[2]}")

                # User registration
                event_id = int(input("Enter the ID of the event you want to register for: "))
                participant_name = input("Enter your name: ")
                query = "INSERT INTO participants (event_id, participant_name) VALUES (?, ?)"
                self.db.stmt.execute(query, (event_id, participant_name))
                self.db.conn.commit()
                print(f"You have been successfully registered for the event!")
            else:
                print("No upcoming adoption events.")
        except pyodbc.Error as e:
            print(f"Error managing adoption events: {str(e)}")
        except ValueError:
            print("Invalid input. Please enter valid information.")
        finally:
            self.db.close()
