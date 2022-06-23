class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
        

dog = Dog("Fido", 8)
dog1 = Dog("Jasper", 5)

print(dog.get_name())
print(dog.get_age())

print(dog1.get_name())
print(dog1.get_age())

