#Create a simple calculator - ask two numbers and an operator (+, -, *, /) and show
num1 = int(input("enter your 1st number"))
num2 = int(input("enter your 2nd number"))
operator = int(input("enter 1 for +, enter 2 for -, enter 3 for *, enter 4 for /"))
if operator == 1:
    print(num1+num2)
elif operator == 2:
    print(num1-num2)
elif operator == 3:
    print(num1*num2)
elif operator == 4:
    print(num1/num2)
