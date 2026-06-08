#Ask user for their age and print whether they are a child, teenager or adult
age = int(input("enter your age"))
if age < 14:
    print("you are a child")
elif age > 14 and age < 18:
    print("you are a teenager")
else:
    print("you are an adult")
