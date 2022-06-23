class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old")

    def speak(self):
        print("I'm a pet")
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I'm {self.name} and I'm {self.age} years old and I'm {self.color}")

class Dog(Pet):
   
        
    def speak(self):
        print("Woof")

class Fish(Pet):
       pass

pet = Pet("david", 4)
dog = Dog("Fido", 2)
cat = Cat("Garfield", 1, "orange")
# dog.speak()
# cat.speak()
# dog.show()
# cat.show()

# pet.show()
# pet.speak()

fish = Fish("Nemo", 1)
fish.speak()

cat.show()