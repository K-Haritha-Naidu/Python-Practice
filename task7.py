#Ask user to enter a number and print its factorial
num = int(input("enter a number"))
for i in range(1, num):
    num = num * i
print(num)
