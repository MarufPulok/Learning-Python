class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average(self):
        pass

s1 = Student("John", 18, "A")
s2 = Student("Jane", 18, "B")
s3 = Student("Joe", 18, "C")

c = Course("Python", 2)
c.add_student(s1)
c.add_student(s3)

print(c.students[1].name)
print(c.add_student(s2))