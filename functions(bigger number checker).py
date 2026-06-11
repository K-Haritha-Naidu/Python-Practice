#Write a function called bigger that takes two numbers and prints whichever one is bigger.
num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
def bigger_number(num1,num2):
    if num1 > num2:
        print("the bigger number is:", num1)
    elif num1 < num2:
         print("the bigger number is:", num2)
    else:
        print("both are equal:)")
bigger_number(num1,num2)
