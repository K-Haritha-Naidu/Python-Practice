#Function that checks if a word is a palindrome
word = input("enter a word:")
def palindrome(word):
    if word[::-1] == word:
        print("the given word that is palindrome is:",word)
    else:
         print("the given word that is not palindrome is:",word)
palindrome(word)
