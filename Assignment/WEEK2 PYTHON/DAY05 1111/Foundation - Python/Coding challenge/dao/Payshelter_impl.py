import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBConnection import dbConnection
from entity.Pet import Pet
from entity.PetShelter import PetShelter

class PetShelter_impl(PetShelter):
    def __init__(self):
        self.db = dbConnection()

    def add_pet(self, pet):
        self.db.open()
        query = "INSERT INTO pets (name, age, breed) VALUES (?, ?, ?)"
        self.db.stmt.execute(query, (pet.name, pet.age, pet.breed))
        self.db.commit()

    def fetch_available_pets(self):
        self.db.open()
        query = "SELECT name, age, breed FROM pets"
        self.db.stmt.execute(query, (pet.name, pet.age, pet.breed))
        rows = self.db.stmt.fetchall()
        pets = [Pet(row[0], row[1], row[2]) for row in rows]
        return pets

    def remove_pet(self, name):

        self.db.open()
        query = "DELETE FROM pets WHERE name = ?"
        self.db.stmt.execute(query)
        self.db.commit()
        self.connection.commit()  