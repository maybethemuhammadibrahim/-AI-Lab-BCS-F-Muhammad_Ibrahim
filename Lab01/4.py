
def inputAndCalc(op):
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    if(op==1):
        return num1+num2
    elif(op==2):
        return num1-num2
    else:
        print("Invalid OP")

input_ = 0
while(input_ != 3):
    print("1.Add 2 nums\n2.Sub 2 nums\n3.Exit")
    input_ = int(input("Enter your choice: "))
    if(input_==1 or input_==2):
        result = inputAndCalc(input_)
        print("Result: ", result)
    elif(input_==3):
        print("Exiting")
    else:
        print("Invalid Choice")

