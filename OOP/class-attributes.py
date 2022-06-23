from ast import Num


class Person:
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod    
    def showNumberOfPeople(cls):
        print(f"There are {cls.number_of_people} people")
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1
        

p1 = Person("John")

p2 = Person("Jane")

p3 = Person("Joe")

Person.showNumberOfPeople()