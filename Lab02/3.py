class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def calculate_grade(self):
        marks = self.__marks
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        else:
            return "F"


student1 = Student("Ahmed")
student1.set_marks(85)

student2 = Student("Fatima")
student2.set_marks(72)

print("Student 1:")
print("Name:", student1.name)
print("Marks:", student1.get_marks())
print("Grade:", student1.calculate_grade())

print()
print("Student 2:")
print("Name:", student2.name)
print("Marks:", student2.get_marks())
print("Grade:", student2.calculate_grade())
