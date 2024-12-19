class PetShelter:
    def __init__(self):
        self.available_pets = []
        
    @staticmethod
    def add_pet(self,pet):
        self.pet=pet
        self.available_pets.append(self.pet)

    def remove_pet(self, pet):
        self.available_pets.remove(pet)

    def list_available_pets(self):
        for pet in self.available_pets:
            print(pet)
