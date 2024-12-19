import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.Pet import Pet
class Dog(Pet):
    def __init__(self, name: str, age : int, breed : str, dog_breed : str):
        super().__init__(name, age, breed)
        self.dog_breed = dog_breed
    @property
    def dog_breed(self):
        return self._dog_breed

    @dog_breed.setter
    def cat_color(self, dog_breed):
        self.dog_breed = dog_breed


def __str__(self):
        return super().__str__() + f", Dog Breed: {self.dog_breed}"
