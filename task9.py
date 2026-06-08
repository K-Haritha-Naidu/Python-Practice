#Count how many vowels are in a word entered by the user
word = input("enter a word")
vowels = ["a","e","i","o","u"]
counter = 0
for n in word:
    if n in vowels:
        counter = counter + 1
print(counter)
