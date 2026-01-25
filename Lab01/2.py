
def dispAndCountEvenNums(num):
    print("Even Nums: ")
    no = 0
    for n in range(1,num+1):
        if n%2 == 0:
            print(n)
            no+=1
    return no


num = int(input("Enter a number: "))
noOfEvenNums = dispAndCountEvenNums(num)
print("Total Even Nums:", noOfEvenNums)

