"""Password generator.
it will generate a password according to
length given by user."""
import string
import random
x = string.ascii_uppercase
x1 = string.ascii_lowercase
x2 = string.digits
x3 = string.punctuation
words = []
words.extend(x)
words.extend(x1)
words.extend(x2)
words.extend(x3)
print("Long password are difficult to hack")

choose = input("Enter 1 if you want create a password"
               " & 2 to secure or modify your password : \n")
if choose == "1":
    while 1:
        print("\npress q to Quit")
        length = input("Enter length of password you want to generate : ")
        if length == "q":
            break
        print("Password is : ","".join(random.sample(words,int(length))))
elif choose == "2":
    """It will make your password unguessable"""
    secure = ( ('s','$') , ('and','&') , ('a','@'), ('o','0') , ('I','!'), ('*',"#") )
    password = input('Enter your password should have at least 8 characters: ')
    for a,b in secure:
        password = password.replace(a,b)
    print("Your secured password is : ",password)

else:print("Wrong input")




