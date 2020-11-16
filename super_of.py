class Person:
    def greet(self):
        print("i am a person")

class Person1:
    def greet(self):
        print("i am a person1")

class Teacher(Person):
    def greet(self):
        super().greet()
        print("i am a Teacher")

class Student(Person):
    def greet(self):
        super().greet()
        print("i am a Student")

class TeachingAssistent(Student, Teacher):
    def greet(self):
        super().greet()
        print("i am a Teaching Assistant")

ta=TeachingAssistent()
ta.greet()