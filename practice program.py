"""
                   your age in 2090
write a program that take int input from user,the input may be age
like 15,81 20 etc... or DOB like 24.1.19 or 15.2.20 etc

1st - your program should recognise whether the input is age or DOB
2nd - then tell them when they are going to attain an age of 100

you are not allowed to us any type of module

4th - ask them whether they want to know what will be their age
      after a give period of time

5th - handle some errors like *you are not yet born
                              *you seems to oldest person alive
                              * you can handle other errors if possible
"""
# user = int(input("\t\t\tenter your age or D.O.B :"))
#
# if len(str(user))==4:ageyear = True
#
# else: ageyear = True
#
# if user > 2021:print("plz born first"),exit()
#
# elif user<1800 and ageyear == True: print("wow! you are the oldest person alive")
#
# if ageyear == True:
#     ageyears = 2021 - user
#     print(f"you will be 100 yrs in {ageyears+100}")
# else:print("something went wrong")







"""
problem no - 2
divide the apple

harry potter has got 'n' number of apples .
harry has some number of students an he has to distribute 
the apples among them equally.he can request more or less
apples if apples provided is excess or less.

you have to take 3 inputs,n - number of apples
mn - minimum number ,mx - maximum number.

Example - 
        input :
        take n,mn and mx as input from user
output : 
    print whether mn and mx divisible or not
    and then print in the pattern below
     if n is 20 ,mn=2 and mx=5
    print:
    2 is divisible by 20
    4 is divisible by 20
    5 is divisible by 20
   
"""
##to apply this logic with n,mn,mx
# i=2
# while i<=5:
#     if i%2 == 0 :
#         print(i)
#     i = i+1


# n = int(input("enter the total number : "))
# mn = int(input("enter minimum number : "))
# mx = int(input("enter the maximum number : "))
# while mn<=mx:
#     if mn%2==0 or mn%mx==0 :
#         print(f"{mn} is divisible by {n}")
#     else : print("nothing is divisible")
#     mn = mn+1







"""
foods and calories

you visit a resturant called 'demon's angel'. and food iteams
are sorted on the basis of calories present in them.
you have to reverse the list in 3 different ways.

1 - `using any inbuilt module
2 - by slicing method
3 - by swapping 1st element with last,2nd element with 2nd last
    element and so on... .
    
    eg - [2,5,8,16,32]
     1st swap swapping 1st element with last
         [32,5,8,16,2]
    2nd element with 2nd last
         [32,16,8,5,2]
so take a list as input and print reversed list 
"""

# list = ["demon","dracula","lucifur","777","maze"]

##slicing method
# a=list[::-1]#by default index is [0:4:-1]
# print(a)

##inbuilt module/method
# list.reverse()
# print(list)


##swaping method
# list[0],list[4]=list[4],list[0]
# list[1],list[3]=list[3],list[1]
# print(list)


##advance swap
# lists = ["demon.0","dracula.1","lucifur.2","777.3","maze.4"]
# for i in range(0,int(len(lists)/2)):#number of times swap
#
#     "swapping elements"
#     lists[i] , lists[len(lists) - i-1 ] = lists[len(lists)- i-1 ] , lists[i]
# print(lists)






"""
extra practice problem
triangle pattern programs
"""
# 1st pattern
# for i in range(1,6):
#     for j in range(i,6):
#         print(j,end="")
#
    # print()# for a new line

#2nd pattern
# for i in range(1,10):
#     for j in range(1,i):
#         print(j,end="")
#     print()# for a new line

#3rd pattern
# for i in range(1,5):
#     for j in range(1,5):
#         if():
#             pass
#     print()# for a new line




"""
find next palindrome

user will input a number or numbers and we have to find next pallaindromne
of the number.
"""
# to find next palliandrome of a number

# def nextpalliandrome(x):
#     x=x+1
#     while True:
#         if str(x) == str(x)[::-1]:
#             return x #return to nextpalliandrome(x)
#         else: x = x+1
#
# if __name__ == '__main__':
#     a=int(input("enter total number of inputs you want to give : "))
#     b = input(input("enter number of palliandrome you want to find out of a number"))
#     palliandrome = []
#
#     for i in range(a):
#         user = int(input("enter the number : "))
#         palliandrome.append(user)
#
#     for j in range(a):
#          print(f"The next palliandrome {b}"
#                f" of number {palliandrome[j]} is {nextpalliandrome(palliandrome[j])}")
#



"""palindromify the list"""
'''
you have a list that contain some numbers.you have to print a list of next palindrome
only those numbers which is greater than 10 otherwise you will print that number.

Input - [1,6,84,93]
Output - [1,6,88,99] 
'''
# def next_palindrome(x):
#
#     while True:
#         if x>=10:
#             x=x+1
#             if str(x) == str(x)[::-1]:
#                 return new_paliandrome.append(x)
#
#         else: return new_paliandrome.append(x)
#
# if __name__ == '__main__':
#     '''take input'''
#     palindrome = []
#     new_paliandrome =[]
#
#     i = int(input("enter the number of items you want to give - "))
#
#     for j in range(i):
#         f = int(input(f"Enter your {j+1}st/nd/rd/th element - "))
#         palindrome.append(f)
#
#     for q in range(i):
#         next_palindrome(palindrome[q])
#
#     print("your list is - ",palindrome,"new palindrome's list is - ",new_paliandrome)

"""                                   LOGIC -
first we took input some some numbers and then stored those in an empty list named palindrome.
and then we created one more empty list named new_palindrome so that we can store the numbers
after modified or unmodified in new_palindrome and then display.
"""








"""              GUESS THE NUMBER
generate a random integer between a and b.
you and your friend will guess that random number between a and b.
you are player1.so, you will play first.player 1 have to keep guessing the number
until and unless he guess the number.After player1 player2 will guess the number.
the person who take least number of guesses will win.
also if a player will quit other player will win automatically. 
"""

# import random
# random = random.randint(0,10)
#
# def player1():
#     x = 0
#     while True:
#         x=x+1
#
#         print("press 69 to quit\n")
#         guess = int(input(f"player1:\nguess a number between 0 and 10 : "))
#
#         if guess == random:
#                 print("you finally guessed,player1\n")
#                 break
#         elif guess == 69:
#                 print("player 1 has been quited\n")
#                 break
#         elif guess > random:
#                 print("\t\tguess a shorter number\n ")
#         elif guess < random :
#                 print("\t\tguess a greater number\n")
#
#     if guess ==69:
#         print("Its ok!")
#
#     else : print(f"no of guesses are {x}")
#     return x #return value of x to (x=0) outside while loop
#
# def player2():
#
#     print("now its the turn of player2\n")
#     x1=0
#     while True:
#         x1=x1+1
#
#         print("press 69 to quit\n")
#         guess = int(input(f"player2:\nguess a number between 0 and 10 : "))
#
#         if guess == random:
#             print("you finally guessed,player2\n")
#             break
#         elif guess == 69:
#             print("player 2 has been quited\n")
#             break
#         elif guess > random:
#             print("\t\tguess a shorter number\n ")
#         elif guess < random:
#             print("\t\tguess a greater number\n")
#
#     if guess == 69:
#         print("Its ok!")
#     elif guess == 1:
#         print(" WOW !")
#     else:print(f"no of guesses are {x1}")
#     return x1
#
#
# if __name__ == '__main__':
#
#     g1=player1()
#     g2=player2()
#
#     if g1<g2:
#         print(f"HURRAY player1 won")
#
#     elif g2>g1:
#         print(f"HURRAY player1 won")
#
#     else : print("tie")
#





"""Detection of error in multiplication table 



Rohan Das is a fraud by nature.

Rohan Das has wrote a python function to print a to a multiplication table
of a given number but it print one of the values (randomly) as wrong.

Rohan Das did this to top in exam by fooling his friends.You cannot tolerate.
So you decided to write a programme that validates Rohan's multiplication table

Your function should be able to find the wrong values in Rohan's table and expose
him as fraud.

Note : Rohan's function return a list of numbers like

Rohan : Input

    Rohan's table , Enter  value = 6
    
Rohan : Output
    Rohan's table = [6,12,19,24.....60]

In the above table of 6 value of 6*3 should be 18

Write a function iscorrect(table,number) and return the index where Rohan's table is
wrong and print it in screen. IF table is completely correct return None
"""




# def iscorrect(table,number):
#     u=user
#     new_table = [ ]
#
#     for i in range(0,11):
#         new_table.append(i*u)
#
#     print(f"Correct table - {new_table}")
#
#     for i in range(1, 11):
#         if new_table[i] != r_table[i]:
#             print(f"{r_table[i]} is wrong it should be {new_table[i]}")
#
#
#
# if __name__ == '__main__':
#     user = int(input("Enter the table number you want : "))
#
#     # rohan,s table
#     import random
#     r = random.randint(1,10)
#     # print(r)
#     r_table = [i*user for i in range(0,11)]
#
#     #Without list comprehension
#     # i = 0
#     # while i <= 10:
#     #     r_table.append(i * user)
#     #     i += 1
#
#     r_table[r] = random.randint(5,50)
#
#     print(f"Rohan's table - {r_table}")
#
#
#     iscorrect(r_table,user)






"""                Jumble words:
Its a result day and everybody is not happy.So,we have to make them 
laugh by jumbling their name.

Your program should take the number of names and separate them by space
as input.Output should be funny names.

Input : 
Enter number of friends :
    3 
    
Enter names of friends : 
    Rohan Das
    Subham Arora
    Rohit Agarwal 

Output :
    Rohan Arora
    Subham Agarwal
    Rohit Das
    
"""

# def funny_name(fname,lname,names):
#
#     for x in fname:
#         for j in lname:
#
#             import random #after break a new random number'll be generated
#             r = random.randint(0, names-1)
#
#             if fname.index(x) != lname.index(lname[r]):
#                 print(f"{x} {lname[r]}")
#                 break
#
# if __name__ == '__main__':
#     names = int(input("Enter number of friends want to give their names for the games:\n"))
#
#     Name_list = [str(input(F"Enter full name of {i+1} friends : ")) for i in range(0,names)]
#
#     #split names into fname and lname
#     fname = []
#     lname = []
#
#     for l in Name_list:
#         a,b = l.split(" ")
#         fname.append(a)
#         lname.append(b)
#
#     funny_name(fname,lname,names)


"""suppose you are a shopkeeper and you want a calculator
it will take numbers and when you will press 'q' it will
give total"""



# sum = 0
# while True :
#     user = input("Enter price of the item : ")
#     if user != 'q' :
#         sum = sum + int(user)
#         print(f"Ordered so far worth {sum}")
#     else:break
#
# paid = int(input("Enter amount paid : "))
#
# print(f"Total price {sum} . ")
#
# if paid > sum:
#     returned = paid - sum
#     print(f"customer paid {paid} . Money returned {returned}")
# else:     print(f"customer paid {paid} . Money returned {0}")




"""Calculate factorial of a given number and then find number of trailing
zeros in that factorial."""
#find factorial of a number.
# i = 1
# user = int(input("Enter the number you want to find the factorial of : "))
# j = 1
# zeros = 0
# while i <= user:
#     k = i * j
#     j=k
#     i = i+1
#
#     #find no of zeros in factorial of a number
#     if i % 5 == 0 :
#         zeros = zeros + 1
# print(f"So number of trailing zeros in factorial of {user} is {zeros}"
# f" and its factorial is {k}")



"""Currency Convertor
data is in 'currency details' folder.
"""

'''store them in list not dict'''
# with open("currency details") as f:
#
#     #Store currency and its value in dict
#     currencydict = {}
#     for i in f:
#         a,b,c = i.split("	")
#         currencydict.update({a:b})
#
# print("List of currencies : ")
# for x in currencydict.keys() : print(x)
# currency_name = input("Copy and paste the name of currency from above in which you want to convert : ")
# amount = int(input("Enter your amount in  INR  : "))
#
# # print(currencydict[user])#access values of key
#
# convert = amount * float(currencydict[currency_name])
# print(f"\n{amount} Rupees is = {convert} {currency_name}")
#
#
#
# """OR (NOT RECOMMENDED)"""
# #here if you type in same currency you will get wrong output
# with open("currency details") as f:
#
#     currencydict = {}
#     for i in f:
#         a,b,c = i.split("	")
#         currencydict.update({a:b})
#
#     for x,y in currencydict.items():
#         currency = input("Enter the currency name in which you want to convert : ")
#         amt = int(input("Enter the amount"))
#         convert = amt * float(y)
#         print(convert , currency)
#         break









