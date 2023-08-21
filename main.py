#TODO Calculator FUNCTIONS




def addition(a,b):
  result=a+b
  return result      
def calculate(a, b, operation):
        #TODO (CONTINUE ON THE SAME PATTERN
        if operation.lower()=="add":
          addition(a,b)



num1 =int(input("enter num 1: "))
num2 =int(input("enter num 2: "))
op = input("enter the operation\n(add/sutract/multiplay/divide):")
print(calculate(num1, num2, op))
