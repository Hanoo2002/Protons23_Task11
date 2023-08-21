num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
op=input("addition,multiplication,subtraction,division: ")
def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

if op=="addition":
    print(addition(num1,num2))

if op=="subtraction":
    print(subtraction(num1,num2))