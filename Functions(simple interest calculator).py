#Write a function called simple_interest that takes principal, rate and time and prints the simple interest.
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("the simple interest is:", si)

p = int(input("enter principle: "))
r = int(input("enter rate: "))
t = int(input("enter time: "))
simple_interest(p, r, t)
