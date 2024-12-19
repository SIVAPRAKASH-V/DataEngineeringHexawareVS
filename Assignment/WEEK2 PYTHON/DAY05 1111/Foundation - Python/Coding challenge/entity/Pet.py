class Pet:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self.breed = breed

    # Getters
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_breed(self):
        return self.breed

    #setters
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if age >= 0:
            self.age=age
        else:
            raise ValueError("Age cannot be negative")

    def set_breed(self, breed):
        self.breed = breed

    #To string method
    def __str__(self):
        return f"Pet(Name: {self.name}, Age: {self.age}, Breed: {self.breed})"


