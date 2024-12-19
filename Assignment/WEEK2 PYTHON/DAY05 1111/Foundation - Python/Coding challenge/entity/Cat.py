import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.Pet import Pet

class Cat(Pet):
    def __init__(self, name, age, breed, cat_color):
        super().__init__(name, age, breed)
        self.cat_color = cat_color

    @property
    def cat_color(self):
        return self.cat_color

    # Setter for cat_color
    @cat_color.setter
    def cat_color(self, cat_color):
        self.cat_color = cat_color
