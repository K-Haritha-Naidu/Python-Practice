#Print the fibonacci sequence up to 10 number
a = 0
b = 1
for i in range(0,11):
    print(a)
    next = a + b
    a = b
    b = next
