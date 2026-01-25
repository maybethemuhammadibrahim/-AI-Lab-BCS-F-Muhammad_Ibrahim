
def calc_avg(marks):
    sum = 0
    for mark in marks:
        sum += mark
    return sum/len(marks)

marks = []
vals = int(input("Enter num of values: "))
for i in range(vals):
    mark = int(input("Enter: "))
    marks.append(mark)

result = calc_avg(marks)
print("Result: ", result)

