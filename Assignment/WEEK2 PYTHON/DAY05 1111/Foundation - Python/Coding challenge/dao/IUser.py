import sys
import os
import pyodbc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBConnection import dbConnection
from dao.Payshelter_impl import PetShelter_impl
from entity.Pet import Pet
from entity.PetShelter import PetShelter
from exception.InvalidPetAgeException import InvalidPetAgeException
from exception.AdoptionException import AdoptionException


class IUser(PetShelter_impl):
    def __init__(self):
        self.db = dbConnection()

    def add_pet(self):
        try:
            self.db.open()  
            name = input("Enter pet name: ")  
            age = int(input("Enter pet age: "))  
            breed = input("Enter pet breed: ")  
            query = "INSERT INTO pets (name, age, breed) VALUES (?, ?, ?)"
            self.db.stmt.execute(query, (name, age, breed))  
            self.db.conn.commit()  
            print(f"Pet '{name}' has been added to the shelter.")
        except pyodbc.Error as e:
            print(f"Error adding pet: {str(e)}")
        except ValueError:
            print("Invalid input for age. Please enter a valid number.")
        finally:
            self.db.close()

    def adopt_pet(pet_name, Petshelter):
        if pet_name not in PetShelter:
            raise AdoptionException(f"The pet '{pet_name}' is not available for adoption.")
        PetShelter.remove(pet_name)  
        print(f"You have successfully adopted '{pet_name}'!")

    def display_pet_listings(self):
        # """Retrieve and display the list of available pets from the database."""
        try:
            self.db.open()
            query = "SELECT name, age, breed FROM pets"
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
