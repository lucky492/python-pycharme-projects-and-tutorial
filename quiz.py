"""quiz"""

"""design a dictionary that take input from user and return the meaning of word from dictionary """
#d = {"k":"hgh"}
#name = input("enter the sting : ")
#print(d[name])




'''INPUT A NUMBER I.E;AGE,IF HE IS ABOVE 18 SAY HE CAN DRIVE OTHERWISE,HE CAN'T 
DRIVE IF AGE IS LESS THAN 18 BUT iF HiS AGE IS EQUAL TO 18 print
COME LATER '''

# i =int(input("enter you age : "))
#
# if 18 < i <= 100:
#    print("you can drive ")
#
# elif i<18:
#    print("you cannot drive")
#
# elif i==18:
#     print("come later")
#
# else:
#    print("invalid number")




# '''faulty calculator
# design a faulty calculator that take input from user and do calculations
# and give error when 45*3 as 555 , 56+9 as 77 , 56/6 as 4 but do not ue any functions'''
#
# num1 = int(input("enter your first number : "))
# num3 = input("enter your sign +,-,* or / : ")
# num2 = int(input("enter your second number : "))
#
# if num1 == 45 and num3 == '*' and num2 == 3:
#     print("555")
#
# elif num1 == 56 and num3 == '+' and num2 == 9:
#     print("77")
#
# elif num1 == 56 and num3 == '/' and num2 == 6:
#     print("4")
#
# elif num3 == '+':
#     print(num1 + num2)
#
# elif num3 == '*':
#     print(num1 * num2)
#
# elif num3 == '-':
#     print(num1 - num2)
#
#   #we can also do divide as below
# elif num1 / num2:
#     print(num1 / num2)
#
# else:
#     print("out of range")

'''
write a program that take input as integer(i) and print pattern
if input is 1 then print below pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
if input is 2 then print below pattern
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
otherwise print invalid
'''
# n = int(input("enter a number "))
#
# if n==1:
#     i=1
#     while i<=5:
#         j=1
#         while j<=i:
#             print(j,end=" ")
#             j=j+1
#         print()
#         i=i+1
#
# elif n==2:
#     i=1
#     while i<=5:
#         j=5
#         while j>=i:
#             print(j,end=" ")
#             j=j-1
#         print()
#         i=i+1
#
# else:
#     print("invalid")

'''write a program which give a number as 5 to guess(5 times),
it take input from user and tell him that inputed number is greater or smaller than the 
number inputed (as 5) in program already and how many guesses are left'''

# print("guess a number between 0 and 50")
# g=0
# #number = 20
#
# while g<=5:#g represent guess number
#
#     num = int(input("enter a number : "))
#
#     if 20>num<=50:
#         print("increase the value")
#
#     elif 20<num<=50:
#         print("decrease the value")
#
#     elif num == 20:
#         print("you won")
#         print(g ,"no of guess took to finish") #shows hom many tmes you guessed to give correct answer
#         # g shows how many times while loop works to finish
#         break
#
#     else:
#         print("you cannot enter more than 50")
#
#     print(6 - g,"no of guess left")
#
#     """when 1st guess is wrong
#         6 - g (6-1)# here 1 repreent while loop run 1 time
#         when 2nd coice s wrong
#         6 - g is (6-2)#here 2 shows while loop runs second times bcz no condition is true
#         if the guessed no is right (6-g) will not be executed bcz
#         when num == 20 control move out of while loop to last
#     """
#     g=g+1
#
# print("game over")
# print("no of guess finished")





"""
CODING SNAKE,WATER,GUN GAME.ITS LIKE STONE PAPER SCISSOR.

if you made snake    and other made water
    snake will drink water and you win

if you made water    and other made gun
     gun will immerse in water and you win
     
if you made snake     and other gun
     gun will kill snake and you loose

here other guy is computer

now design a program or game that choose what you want to take
snake,water or gun . 's' for snake and 'w' for water and 'g' for gun .
and pc will choose any one randomly.

1st you will ask what will you choose s,w,or g
if you enter any one pc will choose any one randomly.
and winner will be displayed.(you vs pc)

this game continue 10 times

after that at last display whose points are more you or pc.
and declare the winner and also declare how many times you won
and how many time pc won
"""


# """  snake water and gun game  """
#
# list = ["s" , "w" , "g"]
# import random
#
# pc_point = 0
# user_point = 0
#
#
# no_of_choice = 0
# while no_of_choice <10:
#
#     choose = input("enter s,w or g : ")
#     randoms = random.choice(list)
#     print(randoms)
#
#     if choose ==  randoms:
#         print("it's a tie both ae very strong characters")
#
#
#    # for snake
#     elif choose == "s" and randoms == "w":
#         user_point = user_point +1
#         print(f"now pc point is {pc_point} and user point {user_point}")
#         print("you won as snake drank water \n")
#
#     elif choose == "s" and randoms == "g":
#         pc_point = pc_point +1
#         print(f"now pc point is {pc_point} and user point {user_point}")
#         print("computer won as gun killed snake \n")
#
#
#
#    #for water
#     elif choose == "w" and randoms == "s":
#         pc_point = pc_point + 1
#         print(f"now pc point is {pc_point} and user point {user_point}")
#         print("computer won as snake drank water \n")
#
#     elif choose == "w" and randoms == "g":
#         user_point = user_point + 1
#         print(f"now pc point is {pc_point} and user point {user_point}")
#         print("you won as gun sunk in water \n")
#
#
#
#    #for gun
#     elif choose == "g" and randoms == "s":
#         user_point = user_point +1
#         print(f"now pc point is {pc_point} and user point {user_point}")
#         print("you won as gun killed snake \n")
#
#     elif choose == "g" and randoms == "w":
#         pc_point = pc_point + 1
#         print(f"now pc point is {pc_point} and user point {user_point}")
#         print("computer won as gun sunk in water \n")
#
#     else :
#         print("invalid input try again \n")
#
#     no_of_choice = no_of_choice +1
#
#
#
# print("game over \n")
# print(f"your total point is {user_point} and pc total point is {pc_point} \n")
#
# if user_point>pc_point:
#     print("you won")
#
# if user_point<pc_point:
#     print("you lost")
#
# else: print("it's a tie")
#
# print("\t \t \t  thank u for playing ")
#





"""
read news from internet.use news api website


news api key
098e7114f694495b95fe1e1151313a75
"""

# import requests
# import json
# import time
#
# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.speak(str)
#
# if __name__ == '__main__':
#     # speak("today's news is")
#     r = requests.get("https://newsapi.org/v2/top-headlines?"
#                      "country=us&apiKey=098e7114f694495b95fe1e1151313a75").text
#
#     parse_dict = json.loads(r)
#
#     print(json.dumps(parse_dict, indent = 4, sort_keys=True))
#
#
#     a = parse_dict['articles']
#
#     for article in a:
#         speak(article["content"])
#         time.sleep(2)
#         speak("moving onto next article")
#
#     speak("thanks for listening")



"""  EMAIL COLLECTOR"""



# import re
# s = "hello bot jfhd lohitkishnanaik@gmail.com python gf" \
#          "ggd like see di pyr lucynaik2@gmail.com called by ddd" \
#          " demonlucky4@gmail.com ok fie pie rajveersing@gmail.com"

"""
\w matches any non whitespace character
@ for email
+ for repeat a character one or more time
"""
# a = re.findall(r'[\w\.]+@[\w\.]+',s)

# d=['lohitkishnanaik@gmail.com', 'lucynaik2@gmail.com', 'demonlucky4@gmail.com', 'rajveersing@gmail.com']
#
#
# with open('exer','a')as f:
#     l = re.findall(r'[\w\.]+@[\w\.]+',s)
#     i=0
#     k = f'\nemail  = '.join(map(str, l))
#
#     print(k)
#
#     for k in k:
#         f.write(k)
#


"""Find next palliandrome of a given list """
# def next_palindrome(pal):
#
#     for r in range(0,i):
#         a = pal[r]
#
#         while True:
#             a = a+1
#             if str(a) == str(a)[::-1]:
#                 new_paliandrome.append(a)
#                 break
#
# if __name__ == '__main__':
#     '''take input'''
#     palindrome = []
#     new_paliandrome =[]
#
#     i = int(input("enter the number of items you want to give - "))
#
#     for j in range(i):
#         f = int(input(f"Enter your {j+1} element - "))
#         palindrome.append(f)
#
#     next_palindrome(palindrome)
#
#     print("your list is - ",palindrome,", new palliandrome's list is - ",new_paliandrome)







'''
oh soldier prettify my folder



1st make a function named soldier.that take 3 input
as path,file,format.

def soldier(path,file,format):

1st for path - take a path of any folder,file etc...

2nd for path -
        now 
        SELECT ANY PATH and capitalize the first letter of 
        folders in that path.
        for example - in path c:// capitalize first letter of
        all folders in that path but don't change its content.

3rd for format -
        if in that path there would be any names like
        hrry.jpg,shok.jpg,karry.jpg etc...  . write them like
        1.jpg,2.jpg,3.jpg etc....      

'''

'''unfinished'''
# import os
# def soldier(path,file,format):
#
#     os.chdir(path)
#     file = os.listdir(path)
#     i = 1
#
#     with open(file) as f:
#         file_list = f.read().split("\n")
#
#
#     # now iterate files
#     for file in file:
#         if file not in file_list:
#             os.rename(file,file.capitalize())
#
#         if os.path.splitext(file)[1] == format:
#             os.rename(file,f"{i} .{format}")
#             i = i + 1
#
#
#
# soldier(r"C:\Users\user\Desktop\testing folder",
#          r"C:\Users\user\PycharmProjects\newtext.txt",
#          r"txt"
# )




#location
# r"C:\Users\user\PycharmProjects\testing folder",
#         r"C:\Users\user\PycharmProjects\newtext.txt",
#         r"txt"

