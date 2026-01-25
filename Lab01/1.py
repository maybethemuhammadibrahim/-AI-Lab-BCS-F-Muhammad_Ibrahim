
def getGrade(marks):
    if marks >= 85:
        return 'Grade A'
    elif marks >= 70:
        return 'Grade B'
    elif marks >= 50:
        return 'Grade C'
    else:
        return 'Fail'


name = str(input("Enter your name: "))
marks = int(input("Enter your marks: "))
grade = getGrade(marks)
print("Student Name:", name)
print("Marks:", marks)
print("Grade:", grade)