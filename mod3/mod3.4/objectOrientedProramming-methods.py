'''
3.4 Object Oriented Programming - Methods
Name: "Travis Routhier"
github link:"https://github.com/Tarsum67/Python"
'''


class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    def get_kind(self):
        return self._kind

    def set_kind(self, kind):
        self._kind = kind

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        self._breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def print_details(self):
        print(
            f"Pet Details - Kind: {self._kind}, Breed: {self._breed}, Name: {self._name}")


pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Sphynx", "Whiskers")
pet3 = Pet("Bird", "Parakeet", "Sky")


pet1.print_details()
pet2.print_details()
pet3.print_details()


print("\n")
print(f"Is pet1 an instance of Pet? {isinstance(pet1, Pet)}")
