#Write a function called square that takes a number and returns its square
num = float(input("enter the number which you want to square:"))
def square(num):
    squared_number = num*num
    print("the square of the required number is:)",squared_number)
square(num)
