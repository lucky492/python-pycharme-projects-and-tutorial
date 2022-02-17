#guess the number
# print("\t\t\tguess a number between 1 and 10 but you can choose only 5 time")
# i = 0
# num = 5
# while i<5:
#     choose = int(input("choose a number : "))
#
#     if 5>choose<10:
#         print("increase , you are too low")
#
#     elif 5<choose <10 :
#         print("decrease , you are too high")
#
#     elif choose == 5 :
#         print("you won")
#         break
#
#     i = i+1
#
# print("\n\n\t\tthank u for playing")






"""   you vs computer in choosing a number  """
# import  random
# print("\t\t\tguess a number between 1 and 10 but you can choose only 5 time")
# i = 0
# num = 5
# while i<10:
#     rand = int(input(random.randrange(0, 10)))
#
#     if 5>rand<10:
#         print("increase , you are too low")
#
#     elif 5<rand <10 :
#         print("decrease , you are too high")
#
#     elif rand == 5 :
#         print("you won")
#         break
#
#     i = i+1
#
# print("\n\n\t\tthank u for playing")






"    HANGMAN GAME IN PYTHON YOU VS COMPUTER    "

# list = [" ","hack","neck","back","check","nice"," "]
# print(list)
# import random
#
# i= 0
# while i<6:
#     pc = random.choice(list)
#
#     guess = input("guess a 4 digit word from above words: ")
#
#     if guess == pc:
#         print("congrats you won")
#         break
#
#     else: print("try once more")
#
#     i = i+1
#
# print("\t\t\t game over,thanks for playing")
# print(f"the word was '{pc}' ")