dictList = []

for i in range(3):
    d = {}
    d['name'] = input("Enter name: ")
    d['marks'] = int(input("Enter marks: "))
    dictList.append(d)

print("Students Data")
for student in dictList:
    print(student["name"], " : ", student["marks"])

