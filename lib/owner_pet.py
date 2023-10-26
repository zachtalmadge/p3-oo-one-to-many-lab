class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type not in Pet.PET_TYPES:
            raise Exception
        else:
            self.pet_type = pet_type
        Owner.all.append(self)
        Pet.all.append(self)

class Owner:
    
    all = []
    
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        print( [pet for pet in Owner.all])
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            Owner.all.append(pet)
        else:
            raise Exception
    
    def get_sorted_pets(self):
        return sorted(all, key=lambda x: x['name'])