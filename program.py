# in order to execute code remove harshtag sign '#' in program where you need
#or(shortcut) select the area and then press ctrl + /.
#if therea are 2 '#'sign remove one



"""(#) this sign is used to write a single line comment
(""" """ or ''' ''') this sign is used to write multi line comment like a paragraph or essay"""
# # my first program .this is used to write a single line comment
# """this ia a multi line comment which is used to write a big description like paragraph """


#syntax to print or use of print()
#print("hello word ")
#print(5+2+52+1)

#a = 5
#print(a)



'''to join 2 statements using (end=" ")statements'''
"""end statement join 2 different or more statements without giving space in between like
' hello wordpython ' """
#print("hello world",end="")
#print("python")


"""if we leave some space in between like(end=" ")then it give some space 
while joinning 2 different statement in 2 different print()"""
# if we add some space between end ike (end=" ")
#print("hello world",end=" ")
#print("python")


#if we write joker in between colons of end statements(end="joker")
# print("hello world",end="joker")
# print("python")


#OR OTHER SYNTAX TO JOIN TWO LINES
# print("hello world","java",end=" ")
# print("new line")
"""HERE COMMA GIVES SPACE AND JOIN 2 STATEMENTS IN ONE PRINT() BY DEFAULT AND END STATEMENT HELPS TO JOIN OTHER PRINT
STATEMENT IN OTHER PRINT()"""


#print("hello world","java",end=" joker ")
#print("new line")

#IF END STATEMENT IS NOT USED THEN
# print("hello world","java")
# print("new line")



"""VARIABLES IN PYTHON"""
"""VARIABLE IS THE NAME OF THAT IS GIVEN TO ANY STORAGE AREA OR MEMORY LOCATION IN A PROGRAM
ACTUALLY VARIABLE DON'T HOLD THE VALUE BUT IT IS THE NAME GIVEN TO ANY MEMORY LOCATION/ADDRESS IN RAM.
IT MEANS VARIABLE IS A WAY TO ACCESS THAT MEMORY.
VARIABLE IS A BOX THAT CONTAINS INFORMATION,DATA ETC... WHENEVER WE NEED TO ACCESS INFORMATION WE CAN USE CONTAINER
TO ACCESS IT'S CONTENT/INFORMATION"""

#EXAMPLE
#var1 = "python"#HERE PYTHON IS STORED IN VAR1 WHICH IS THE CONTAINER
#print("var1")

"""USE OF TYPE() .  IT TELLS US THE DATA STORED IN VARIABLE IS OF WHICH TYPE(INT /FLOAT/STRING ETC...)"""
#var1 = "python"
#var2 =  5
#var3 = 36.7
#print(type(var1))# IT TELS VAR1 IS OF STRING TYPE
#print(type(var2))#IT TES VAR2 IS OF INT TYPE
#print(type(var3))#IT TELLS VAR3 IS OF FLOAT TYPE

#print((var2+var3))
#print(type(var2+var3))
#print(var1+var3)# error will come because string cant be add with float



"""TYPE CASTING/changing .  it helps to change the type liKe int can be changed to float and vice versa. example"""
#var0 = "56"
#var1 = "12"
#var2 = 4
#var3 = 36.7
#print(int(var0)+int(var1))#var0 and var1 is converted to int
#print(int(var3)+float(var2))
#print(str(var2))

#THERE ARE ALSO STR() INT() FLOAT() DOUBLE() LONG() ETC...




#IF I WANT TO PRINT PYTHON/SOMETHING 10 OR 20 TIMES.THERE ARE 2 WAYS TO DO II.
# FIRST ONE IS TO WRITE PRINT("PYTHON") 10 TIMES OR AS IN BELOW
#print(10 * " python ")
#print(10 * "python\n")# if i want to print python 10 times in different lines then use \n

#if we want to multiply 10 with the sum of var0 and var1.then
#var0 = "56"
#var1 = "12"
#var2 = 4
#var3 = 36.7
#print(10 * int(var0)+int(var1))
#print(25 * float(var2)-int(var3))

#if we want to print the sum of var0 & var1 10 times.THEN
#print(10 * str(int(var0)+int(var1)))
'''at 1st var0 and var1 will be convered to int and then to string and print 10times.
if i don't convert var0 and var1 to string 10will be multiplied to them.but 10 cant be multiplied with a sting'''





"""STRINGS"""
# anything within double code(" ") is a string
#mystr = "the demon king"
#print(mystr) #to print a string

"""NOW IF WE WANT TO PRINT 'h' FROM  mystr = "the demon king" THEN WE NEED TO KNOW THE INDEX 'h' 
AND BY GIVING THE INDEX OF NUMBER WE CAN PRINT 'h' .INDEX START FROM AND LENGTH START FROM 1 ."""
"""SLICING IN PYTHON"""
#mystr = "the demon king"
#print(mystr[1])
#print(mystr[5])

#now if we want to print demon from "the demon king" then the format is
#mystr = "the demon king"
#print(mystr[0:3])
"""here 0 is the index of string and 3 is the length of string of which count start from 1.it says print from 
index 0 to length 5"""
#print(mystr[4:9])# print from index 0 to length 5


#print(mystr[0:13])
#print(mystr[0:14])


# advance
#print(mystr[0:50])  #it will give upto how much it is available i.e 13th index (mystr[0:14])

#IF WE WANT TO SKIP ONE CHARACTER AFTER AFTER EVERY ONE CHARACTER OUTPUT SHOULD BE 'dmn'
#mystr = "the demon king"
#print(mystr[4:9:2])
"""here at first 4 to 9 will be printed and then one gap will be skipped and print'dmn' here 2means1,3means2"""
#print(mystr[4:9:1])#here 1maeans0 i.e, no character is skipped
#print(mystr[4:9:3])# here 3 maeans 2 i.e, 2 character will be skipped

#print(mystr[0::2])# by defaut mystr wi be[0:14:2]
#print(mystr[::])
"""by default it will be fist from 0to14 and then last place will be 1 because nothing is given so mystr[0:14:1]"""
#print(mystr[:5:]) # by deault[0:5:1]
#print(mystr[0::])# by deault[0:14:1]
#print(mystr[::3])#by defult[0:14:3]
#print(mystr[::553])#here first it will take index 0to14 and then it will skip upto how much it can skip i.e;14

#print(mystr[0:])
"""by default the last index will be 14.as we have not given any limit so it wi gve upto how much it will be available"""
#print(mystr[:5])# by defaut it will take 0th index
#print(mystr[:])# by default it will take (mystr[0:14])

#IF WE COUNT FROM BACKWARD DIRECTION i.,FROM G TO T THEN INDEX START FROM -1,-2,-3.-4......
#mystr = "harry is a good boy"
#print(mystr[-4:])
#print(mystr[-4:-2])

#print(mystr[::-1])#-1 reverse the string
#print(mystr[::-2])# skip one character from back.-1 reverse the stng and -2 skip one character

"""USE OF FUNCTIONS EXAMPLES  """

"""USE OF len().  IT TELLS THE LENGTH OF STRING"""
#mystr="python"
#print(len(mystr))# LENGTH START FROM 1 BUT INDEX START FROM 0

"""isalnum()  """
#mystr = "harry is a good boy"
#print(mystr.isalnum())
"""OUTPUT IS FALSE BECAUSE mystr IS NOT A ALPHANUMERIC NUMBER I.E; IT CONTAINS SPACE IN BETWEEN SO IT IS NOT ALPHA AND 
IT DOES NOT CONTAIN NUMBER SO IT IS NOT NUMERIC .IF WE REMOVE SPACE IT WILL SHOW SPACE"""

#mystr = "harryisagoodboy"
#print(mystr.isalnum())#IT SHOW TRUE BECAUSE mystr DOESNOT CONTAIN SPACE IN BETWEEN

#mystr = "GADU535736"
#print(mystr.isalnum())#IT SHOW TRUE BCZ IT DOESNOT CONTAIN SPACE SO IT IS ALPHA AND IT CONTAIN NUMBER SO IT IS NUMERIC

"""isapha()      """
#mystr = "harry is a good boy"
#print(mystr.isalnum())
#it shows false because it is neither a alpha no numeric numbe i.e;it contains space so it is not alpha

"""endswith()   """
#mystr = "harry is a good boy"
#print(mystr.endswith("boy"))#RETURNS IN BOOLEAN I.E; TRUE .BECAUSE mystr END SWITH BOY
#print(mystr.endswith("doy"))#RETURNS IN BOOLEAN I.E; FALSE .BEACUSE mystr ENDS WITH BOY NOT DOY

"""count()      """
#mystr = "harry is a good boy"
#print(mystr.count("o"))#IT TELLS HOW MANY TIMES 'O' IS REPEATED

"""capitalse()"""
#mystr = "the demon king"
#print(mystr.capitalize())#IT CAPITALISE THE FIRST CHARACTER 't' INTO 'T'

''' find()   '''
#mystr = "venom is back"
#print(mystr.find("is"))#IT GIVES THE INDEX FROM WHERE THE 'is' STARTED i.e;index of i
#print(mystr.find("back"))#IT GIVES THE INDEX FROM WHERE THE 'back' STARTED i.e;index of b

'''lower()   '''
#mystr = "THUG LIFE"
#print(mystr.lower())# IT CONERTS THE WHOLE STRING TO SMALL LETTER

'''UPPER()   '''
#mystr = "thug life"
#print(mystr.upper())

'''replace()'''
#mystr = "turn down for what"
#print(mystr.replace("what","that"))#REPLACE 'what' WITH 'that'

"""THERE ARE MORE FUNCTIONS IN PYTHON EXPLORE IT IN INTERNET"""





"""  USE OF INPUT().  INPUT() IS USED TO TAKE INPUT FROM USER"""
#print("ENTER A NUMBER")
#inpnum = input()
#print("the inputed number by user is",inpnum)
"""in the above example nput() accept the number fom user and store it in inpnum"""

"""NOW IF WE WANT TO ADD/MULTIPLY/DIVIDE SOMETHING IN THE INPUTED NUMBER OF USER THEN"""
#print("ENTER YOUR NUMBER")
#inpnum = input()
#print("you entered ",int(inpnum)+10)
#inpnum will store number as a string and 10 is an int so at 1st inpnum needs to be converted to int and then add


#ADD TWO NUMBER ENTERED BY USER
#print("ENTER YOUR FIRST NUMBER")
#n1 = input()
#print("ENTER YOUR SECOND NUMBER")
#n2 = input()
#print("sum of two entered number is",int(n1)+int(n2))

#add two stings
#print("enter a strng")
#str1=input()
#print("enter another string")
#str2=input()
#print(str1+str2)








'''LIST IN PYTHON'''
#grocery = ["harpic","deterent","soap","lollypop"]
#print(grocery)  #THIS IS A LIST OF GROCERY AND HOW TO PRINT IT
#print(grocery[0])# THIS IS HOW TO PRINT THE ITEAMS OF GROCERY IN INDEX 0
#print(grocery[3])

#numbers = [65,32,78,12,48]
#print(numbers)
#print(numbers[0])
#print(numbers[1])

#print(numbers.sort())
#here output is showing none.so if we use sort() first then print numbers
#numbers.sort()
#print(numbers)#here sort() arrange the numbers in list in ascending numbers

# if we use reverse()
#numbers.sort()
#numbers.reverse()
#print(numbers)
""" at first sort() print the numbers in ascending order and then reverse() reverse it and the numbers dispayed is in 
descending order"""





'''SLICING'''
#numbers = [65,32,78,12,48]
#print(numbers[0:5])# here 0 is index and 5 is length.print from index 0 to length 5
#print(numbers[:5])# takes index 0 automatically
#print(numbers[:])# takes index o and length automatically
"""in slicing a new list is returned and original list is unaffected .but if we use sort() or reverse() 
the original list also changes like in above"""





'''EXTENDED SLICE'''
#numbers = [65,32,78,12,48]
#print(numbers[::])# by default the first parameter is 0 and second parameter is 5 and 3rd parameter is 1
#print(numbers[::2])

#print(numbers[::-2])
#IF WE DONOT USE DEFAULT AT FIRST AND SECOND PARAMETER THEN IT MAY NOT WORK LIKE A BLANK SPACE COMES
#print(numbers[1:5:-3])# ONLY TAKE -1 OR ABOVE NOT BELOW IT OTHERWISE IT WILL SHOW BLANK LIST LIKE []




'''len() max() min()  etc....'''
#numbers = [65,32,78,12,48]
#print(len(numbers))
#print(max(numbers))
#print(min(numbers))





'''append() . it is used add/insert something at end'''
#numbers = [65,32,78,12,48]
#numbers.append(5)
#print(numbers)

#if we use append() three times
#numbers.append(5)
#numbers.append(5)
#numbers.append(6)
#print(numbers)

#if we use blank list
#numbers=[]
#numbers.append(5)
#numbers.append(5)
#numbers.append(6)
#print(numbers)



'''insert()  it is used to insert something in list anywhere'''
#numbers = [65,32,78,12,48]
#numbers.insert(2,0)# insert 0 at index2
#print(numbers)




'''remove()  it is used to remove something in list'''
#numbers = [65,32,78,12,48]
#numbers.remove(65)
#print(numbers)# remove 65 from list




'''pop()   it remove the last  elements'''
#numbers = [65,32,78,12,48]
#numbers.pop()
#print(numbers)




'''MUTABELE         SOMETHING THAT CAN BE CHANGE IS MUTABLE'''
#numbers = [65,32,78,12,48]
#numbers[2]=0
#print(numbers)# replace 78 with 0
'''IMMUTABLE        SOMETHING THAT CAN'T BE CHANGE IS IMMUTABLE
LIKE TUPLE  -  TUPLE IS A COLLECTION OF PYTHON OBJECTS SEPARATED BY COMMAS EXAMPLE tp = (2,5,8)'''
#tp = (2,5,8)
#print(tp)

"""OUTPUT IF BELOW PROGRAM WILL BE ERROR BECAUSE 4 CAN'T BE REPLACED WITH 5 WHICH IS AT INDEX 1 BECAUSE IT IS 
IMMUTABLE"""
#tp = (2,5,6)
#tp[1] = 4
#print(numbers)

#IF WE ADD A COMMA AT END
#tp = (5,)
#print(tp)# it becomes a tuple if we add comma

# if we do not use comma then it is not a tuple
#tp = (5)
#print(tp)
#



'''SWAPING IN PYTHON'''
'''TRADITIONAL/OLD METHOD IS'''
#a=1
#b=3
#temp=a
#a=b
#b=temp
#print(a,b)
'''IN PYTHON NEW METHOD IS'''
#a=1
#b=3
#a,b=b,a
#print(a,b)

"""SEARCH/EXPLORE MORE LIST FUNCTIONS IN PYTHON"""






'''DICTIONARY IN PYTHON'''






"""DICTIONARY IS NOTHING BUT KEY VALUE PAIRS . PYTHON HAS GIVEN DATATYPES TO MAKE SUCH PAIRS"""
#d1 = {}
#print(type(d1))# shows the d1 is of which type

#d1 = []
#print(type(d1))

#d1 = ()
#print(type(d1))

#HOW TO MAKE AND ACCESS A DICTIONARY
#d1 = {"harry":"eat chocolate","demon":" drink blood","rohan":"eat fish"}
#print(d1)
#D1 IS A DICTIONARY IN WHICH LETS IMAGINE A STORY WHERE HARRY EAT CHOCOLATE AND DEMON DRINK BLOOD AND ROHAN EAT FISH

#NOW IF WE WANT TO ACCESS HARRY / KNOW WHAT HARRY EAT THEN
#d1 = {"harry":"eat chocolate","demon":" drink blood","rohan":"eat fish"}
#print(d1["harry"])# here we can access the elements of dictonary /(we know what harry eat?)
#print(d1["rohan"])

'''BASICALLY HERE IT PRINT KEY VALUES . KEY VALUES MEANS WORD MEANING .
IN ABOVE HARRY IS THE KEY AND EAT CHOCOLATE IS THE VALUE OF HARRY'''





"""WE CAN ALSO KEEP A DICTIONARY WITHIN DICTIONARY"""
#d1 = {"harry":"eat chocolate",
#      "demon":" drink blood",
#     "rohan":"eat fish",
#     "d2":{"arun":"play basketball","das":"pay cricket"}}
"""in above d2 is a dictionary inside dictionary d1 and inside d1 the story is arun plays basketball and 
das play cricket . we can print the elements of d2 by"""
#print(d1["d2"])
''' we can acess the elements of d2's dictionary by'''
#print(d1["d2"]["arun"])#here first d2's dictionary is searched and then arun's value is searched i.e;play baketball

'''here d2 can be a list,dictionary or tuple but the keys are immutable(cant change).keep keys a number or 
string   example --'''

#d1 = {"harry":"eat chocolate",
#     "demon":" drink blood",
#     "rohan":"eat fish",
#     "d2":["this is a list"],
#     "d3":("this is a tuple"),
#      "d4":{"this is a dictionary"}}
#print(d1["d3"])
#print(d1["d2"])
#print(d1["d4"])





'''HOW TO ADD ELEMENTS IN A dictionary   .there are two ways using update() and old method'''
#d1 = {"harry":"eat chocolate",
#     "demon":" drink blood",
#     "rohan":"eat fish",
#     "d2":["this is a list"],
#     "d3":("this is a tuple"),
#      "d4":{"this is a dictionary"}}

#d1["ankit"]= "eat junk food"   #OLD METHOD





'''FUNCTIONS IN PYTHON DICTIONARY'''




'''UPDATE()'''
#d1.update({"ankit":"eat junk food"})  # NEW METHOD USE UPDATE() BEFORE PRINT(),OTHERWISE OUTPUT WILL BE NONE
#d1.update({"420 name ":"one more name added"})
#print(d1)
# ABOVE ANKIT IS PRINTED 1 TIME BCZ PYTHON TAKES UNIQUE NUMBERS I.E; IT DOES NOT REPEAT SOME STRING OR NUMBER 2 TIMES

'''NOW IF WE CREATE D2 & MAKE D2=D1 AND AFTER THAT IF WE MAKE SOME CHANGES IN D3.then'''
#d1 = {"harry":"eat chocolate",
#     "demon":" drink blood",
#     "rohan":"eat fish",
#     "d2":["this is a list"],
#     "d3":("this is a tuple"),
#      "d4":{"this is a dictionary"}}
#d2={}
#d2=d1
#print(d2)
'''from above  d2 is a pointer whch point dictionary d1 and d2 is also a pointer which point on itself.
d2 is a reference of dictionary d1 .any changes in d2 will affect d1 '''

'''del    word   . to delete something from list.whatever deleted from d2 will be also deleted from d1'''
d1 = {"demon":" drink blood",
     "rohan":"eat fish",
     "d2":["this is a list"],
     "d3":("this is a tuple"),
      "d4":{"this is a dictionary"}}
#d2 = {}
#d2= d1
#del d2["demon"]
#print(d2)
'''IF WE  WANT TO DELETE "demon" FROM d2 AND DON'T WANT TO DELETE FROM d1THEN USE COPY().
IF WE SOMETHING FROM D2 FROM D1 THAT THING WILL NOT BE DELETED '''
'''copy()'''
#print(d1.copy())  #copy() copy d1

''' get()'''
#print(d1.get("demon")) # demon's value will be printed

'''keys()'''
#print(d1.keys()) # says the keys name in dictionary

'''items()'''
# print(d1.items())  # says the value of keys

"""EXPLORE OR SEARCH MORE PYTHON DICTIONARY FUNCTIONS"""





'''SET IN PYTHON'''

#s = set() # syntax to create set .dont forget to write set before paranthesis'()' i.e; s=set()
#print(type(s)) # this is how to know that it is a set by using type()

#s = set({5,8})
#print(type(s))

'''MAKE A SET USING LIST'''
#s_from_list = ([5,7,3,9])  #this is a set which contains a list
#print(s_from_list)         # this is how to print a set
#print(type(s_from_list))   # this show set





'''TO ADD ELEMENTS IN A SET  using add()'''
#s = set() # l is a blank set
#s.add(3)
#s.add(3)
#s.add(5)
#s.add(8)
#print(s)  # 3 is executed only one time because set only take unique number





'''functions in set'''

'''len()'''
#s = set() # l is a blank set
#s.add(3)
#s.add(3)
#s.add(5)
#s.add(8)
#print(len(s))#give length 3 not 4 because '3' is executed one time not two time

'''isdisjoint() it say whether s1 and s have same elements or differnt.if true they are different and vice versa '''
#s = set({3,5}) # l is a blank set
#s1 ={3,5}
#print(s.isdisjoint(s1))
#print(type(s))

'''remove()'''
#s = set() # l is a blank set
#s.add(3)
#s.add(5)
#s.remove(5)
#s1 ={3,5}
#print(s,s1)

#now use both remove() and isdisjoint()
#s = set() # l is a blank set
#s.add(3)
#s.add(5)
#s.remove(5)
#s1 ={6,8}
#print(s.isdisjoint(s1)) # yes s and s1 are different

'''union()'''
#s = set() # l is a blank set
#s.add(1)
#s.add(5)
#s.union({1,5})
#print(s)

"""now add 3 in union()"""
#s.union({1,5,3})
#print(s)
"""now if assign s.union in a new variabe s1 and print(s,s1)"""
#s1 = s.union({1,5,3})
#print(s,s1)  # first it print s and then s1
"""intersection()   it print common elements in two sets"""
#s1 = s.intersection({1,5,6})
#print(s,s1)

'''SEARCH MORE LIST FUNCTIONS IN INTERNET'''








'''IF ELSE AND ELIF(ELSE IF) STATEMENT'''
#LETS CREATE 2 VARIABLES AND FIND GREATEST AMONG THEM BY USING IF ELSE STATEMENT
#var1 = 5
#var2 = 8

#if var1>var2:       #AFTER GIVING COLON SIGN PRESS ENTER . OR ON DOWN LINE PRESS TAB IT WILL GIVE A BIG SPACE
#    print("yes var1 is greater than var2")
#else:
#    print("var2 is grater than var1")
""" in above at first the condition1 is checked i.e;whether var1 s greater or var2 is greater
if true it print statement1 i.e;'yes var1 is greater than var2'. if condition1 is false then condition2 is
printed"""
""" we can also understand if else by a story like - suppose our mother said us if you will study you
 will pass else you will fail"""

"""NOW LETS TAKE INPUT FROM USER"""
# var2 = 10
# print("ENTER YOUR NUMBER")
# var3 = int(input())   # at first we give input as a string and then it will convert into int
#
# if var3>var2:
#    print("var3 is greater")
# else:
#    print("var 2 is greater")
"""IN THE ABOVE PROGRAM IF WE ENTER 10 IT SHOWS VAR2 IS GREATER WHICH IS WRONG SO WE WILL USE ONE MORE 
CONDITION    I.E;IF var3==var2: """
#var2 = 10
#print("ENTER YOUR NUMBER")
#var3 = int(input("enter :"))

#if var3>var2:
#    print("var3 is greater")
#if var3==var2:     #dont use = use == one= is an assignment operator
#    print("var3 is equal to var2")
#else:
#    print("var3 is lesser than var2")






'''ELIF STATEMENT (ELSE IF)'''

"""ON ABOVE PROGRAM IF CONDITION1 IS FALSE IT PRINT MOVE TO SECOND CONDITION BUT IF CONDITION1 IS TRUE
THEN ALSO IT CHECK CONDTION2 .IF THERE WOULD BE 100 IF STATEMENT IT WILL CHECK ALL IF STATEMENT EVEN IF 
ONE CONDTION AMONG THEM IS TRUE .SO IT MAKE OUR DEBUGGING SLOWER .SO IF WE WANT TO STOP CHECKING ALL 
CONDTION AND COME OUT OF PROGRAM AFTER ONE CONDITION IS TRUE WE USE ELIF STATEMENT (ELSE IF) """

#var2 = 10
#print("ENTER A NUMBER ")
#var3 = int(input())

#if var3>var2:
#    print("var3 is greater")
#elif var3==var2:
#    print("var3 is eaual to var2")
#else:
#    print("var3 is lesser and var2 is greater")
"""if elif (if else if) if condition1 is true it print statement1 and come out of program to give output.
but if condition1 is false it check for condition2 and if condition2 is true it print statement2 
if condition2 is false it print statement3 which is of else"""




"""USE OF 'if in' STATEMENT WITH LIST"""
#list1 = [5,3,7,6]
#if 5 in list1:   #it check whether is list1 if it i present it print statement.if not present it dont print anything
#    print("yes its in list")

"""use of 'if not'  statement"""
#list2 = [5,3,7,6]
#if 56 not in list2:  # it gives true because 56 is not in list
#    print("not in list2")

"""use of 'in' keyword"""
#list2 = [5,3,7,6]
#print(5 in list2) # it gives true if 5 is in list2 otherwise false

#list3 = [5,3,7,6]
#print(56 in list2) # it gives true if 56 is in list3 otherwise false

"""use both 'in' and 'if in' in statement"""
#list4 = [5,3,7,6]
#print(5 in list4) # it gives true if 5 is in list4 otherwise false
#if 5 in list4:     # it  print statement bcz 5 is present in list
#   print("yes it is present")

#list4 = [5,3,7,6]
#print(5 in list4) # it gives true if 5 is in list4
#if 56 in list4:    # it doesnot print statement bcz 56 is not present in list
#    print("yes it is present")



"""use of 'not in' statement"""
#list5 = [5,3,7,6]
#print(56 not in list5) # it gives true if 56 is not in list5

#list6 = [5,3,7,6]
#print(5 not in list6)# it gives false because 5 is in list6 if it will be absent it give true


"""use both 'not in' and 'if not in' statement"""
#list7 = [5,3,7,6]
#print(56 not in list7) # it gives true bcz 56 is not in list7 otherwise false
#if 56 not in list7:     # it  print statement bcz 5 is present in list
#   print("it not is present")

#list8 = [5,3,7,6]
#print(5 not in list8) # it gives false bcz 5 is  in list8 otherwise true
#if 5 not in list8:     # it doesnot print statement bcz 5 is present in list
#   print("it not is present")

#list9 = [5,3,7,6]
#print(5 not in list9) # it gives false bcz 5 is  in list9 otherwise true
#if 56 not in list9:     # it  print statement bcz 56 is not present in list
#   print("it not is present")

#list10 = [5,3,7,6]
#print(56 not in list10) # it gives true bcz 56 is not in list10 otherwise false
#if 5 in list10:     # it  print statement bcz 56 is not present in list
#   print("it  is present")







'''      FOR LOOP      '''






#str = "ha"
#print(str[0])
#print(str[1])

"""suppose we have a string and we want to print all elements individually then we use loop .if we write
it like above it will need a lots of time and if there would be 100 words we cant print it 100 times and it 
will waste time.so it can be replaced with a loop like"""
# for x in "dem":
#    print("x")

"""so above x is a variable and s stores the string .
like in java we write a loop like for(int i=0;i<n;i++)
so in python we write it as     for <a variable name(i)> in <anything in which we want for loop(dem)>:
so in python(inti=0) stands for (i) .then (i<n) stands for 'demo' 
like in java i start from 0 and end with(n) i.e; d is 0 n python and m is 'n'(last index)in python """

"""so at first x is 0 which is 'd' so it print d and then increment/increase by 1
   now x is 1 which is 'e' and it print and then increment/increase by 1
   then x is 2 which is 'm' and then loop stops in java it is 'n' (i<n) """

"""we can also above program as"""
#s = "dem"
#for x in s:  # here x represent "dem" or dem is stored in s and x initialise the index of s
#   print(x)

"""WE CAN ALSO USE FOR LOOP WITH LIST"""

#for i in ["hello","python","world"]:
#    print(i)    # HERE HELLO IS TAKEN AS ONE AND ITS INDEX IS 0 AN PYTHON'S INDEX IS 1

"""WE CAN ALSO WRITE IT AS"""
#list = ["hello","python","world"]
#for i in list:     # here list represent ["hello","python","world"] or it is stored in list variable
#    print(i)

"""now if we want to make a list within list"""
#list1 = [["hello",1],["python",2],["world",3]]
#for i in list1:
#    print(i)

"""if we want to print hello and 1 seperately then for numbers we will use one more keyword"""
#list2 = [["hello",1],["python",2],["world",3]]
#for x,y in list2:# X ACCESS THE INDEX OF STRINGS AND Y ACCESS THE INDEX OF NUMBER
#    print(x,y)

"""if we want to write something in between x and y then - """
#list2 = [["hello",1],["python",2],["world",3]]
#for x,y in list2:# X ACCESS THE INDEX OF STRINGS AND Y ACCESS THE INDEX OF NUMBER
#    print(x,"and",y)

"""if we want to convert list nto dictionary then"""
#list3 = [["hello",1],["python",2],["world",3]]
#d = dict(list3)  # here dict() converted list3 into dictionary
#print(dict)

#for x in d:
#    print(x)

"""if we want to print the keys of dictionary also(1,2 and 3) we have to use items()"""
#list3 = [["hello",1],["python",2],["world",3]]
#d = dict(list3)  # here dict() converted list3 into dictionary
#print(d)
#print(dict)

#for x in d.items():#items()print values of keys(1,2and3).d print the strings and iteam() print numbers
#    print(x)







'''     while loop     '''





#i=0
#while(i<45):
#    print(i)

"""here i will continue printing zero (0) until and unless the condition becomes false i.e; when i will be greater 45
so we need to increment the value of 0 so that when o becomes greater than 45 the condition becomes false and loop 
will stops .so our program is below """
# i=0
# while(i<45):
#    print(i)
#    i = i + 1

"""print from 1 to 45"""
# i=0
# while(i<45):
#     i = i + 1
#     print(i)


"""so if we want to print from 0 to 45 in 1 line then we need to use 'end' statement"""
# i=0
# while(i<45):
#    print(i+1, end=",")  #or print(i+1," , ",end=" ")
#    i=i+1







'''       BREAK STATEMENT       '''






#i=0
#while(True):  #TRUE OR 1 STATEMENT CREATE A NEVER ENDING LOOP
#    print(i)

#i=0
#while(1):
#    print(i)

"""print from 1 to infinity"""
#i=0
#while(True):
#    print(i+1,end=" , ")
#   i=i+1

"""above code print from 1 to infinity to stop it we cn use break statement"""
#i=0
#while(True):
#    print(i+1,end=" , ")
#    i=i+1
#    if (i==20):
#        break  #break statement stops the loop when condition becomes true



'''continue statement'''



"""now if we want to print only those which are less than 5"""
#i=0
#while(True):
#    if i+1<5:
#        continue

#    print(i+1,end=" ")
#    if (i==45):
#        break

"""output is not executed because when i+1<5 control comes down and continue again and agin go up if i+1<5.
when i is greater than 5 it comes down to print statement
output is not coming because we have to update/increase the value of i """
# i=0
# while(True):
#    if i<5 :
#        i = i+1
#        continue
#
#    print(i , end=" ")
#
#    if (i==43):
#        break
#    i = i+1

"""so in above the control comes down from i=0 and check whether i is less than 5 or not 
if i is less than 5 the control comes up because of continue statement
when i is greater than the condition becomes false and control comes down to second
if statement and loop stops when i is equal to 43"""








'''      NESTED WHILE LOOP      '''








"""loop within loop is called nested loop.
syntax    loop:
            loop
"""

# i=1
# while i<=2:
#
#     j=1
#     while j<=3:
#         print( j ,end=" ")
#         j=j+1
#     print()#to print in new line
#     i=i+1

"""when i value is 1 , j print from 1 to 5.
    when i value is 2,j print from 1 to 5.
    when i value is 3 ,j print from 1 to 5"""
"""so here we know that, at first while loop check whether
1 is less than 1 if yes then control comes down and while loop check
whether 1 is less than 3 if yes then control comes down print value of j as 1 
and control comes down and increase the value of j by 1 i.e;to 2 and then control
goes up to 'while j<=3:' and now j=2 and print 2, then j=3 & print3 now when j=4
the condition becomes false and control come down to 'print()' and then i increase to 2

and control comes goes up to  'while i<=2:'  then again control comes down to j and 
print from 1 to 3 in a new line because of 'print()' the i value increase to 3 
then control goes up the condition becomes false then control move out of both loops
i.e;under 'i=i+1' and loop program stops

if we print * instead of printing j 'print('*' ,end=" ")' then output will be
***
***
"""

"""printing square pattern using for loop"""







'''SHORT HAND IF ELSE NOTATION'''

#a = int(input("enter value for a "))
#b = int(input("enter value for b \n"))

#if a<b : print("a is greater")
"""if we want to print if and else statement in one line then"""
#print("a is greter ") if a>b else print("b is greater")






'''FUNCTIONS AND DOCSTRINGS IN PYTHON'''




#a = 9
#b = 1
#c = sum((a,b))
#print(c)

"""in above 'sum()' is an inbuilt function in python to add a and b
we can also create a user defined function which is created/defined by user.
user defined functions are created by using def keyword and then function name"""

#example of user defined funtion
#def function1():
#    print("we are inside  function1")
#print(function1())
"""in output none is also came
if we don't use print() none will not come"""

#def function1():
#    print("we are inside function1")
#function1() #we have to use paranthesis after function1 bcz it's a rule

"""if we want to print we are inside function1 5 times in different places we can do so by just declaring
function name example - """
#def function1():
#    print("we are inside function1")
#function1()
#function1()
#function1()
#function1()
#function1()


"""how functions can take input"""

#def function2(a,b):
#    print("sum of a and b = " , a+b)

#function2(5,5) #input is given
"""we give input as 5,5 ie;in function2(5,5) now control goes up and sore 5,5 in a,b i.e;in function2(a,b)
and print the sum"""



#function to take 3 input and print average
#def function3(a,b,c):
#    avg = (a+b+c)/3
#    print(avg) # return statement store value of avg in v

#function3(5,6,7) # value of function3 is stored in v bcz of return statemen



"""join string in function"""
"""here hello and str(bye) are joined"""
# def function1(str):
#     print("hello" + str)
# function1("bye")
"""if we don't use (+str) after hello then bye will not be join to hello bcz """
# def function1(str):
#     print("hello")
# function1("bye")





''' return statement'''




"""if we want to make a function to store the value of avg in a variable v then"""
#def function3(a,b,c):
#    avg = (a+b+c)/3
     # return statement store value of avg in v

#v = function3(5,6,7) # value of function3 is stored in v bcz of return statement
#print(v)
"""if we want to store value of function3 in a variable named v and print v we get the output as none.
if we want that function3 should return something we need to use return statement """
#def function3(a,b):
#    avg = (a+b)/2
#    return avg
#v = function3(5,7)#user gave input
#print(v)
"""so we give input as 5 and 7 in function3 and now control goes up and store 5,7 in a and b i.e; in function3(a,b) . 
 now average of 5,7 will be stored in avg ,now control comes down and return statement store/return the value in/to
function3(5,7) again from where we gave input and function3(5,7) store it in v and v is printed below.
 so in sort return statement return the value to user again which user has given"""


'''       docstring        '''

#def function3(a,b):
#   """this is the function will calc average"""   #this line is docstring
#    avg = (a+b)/2
#    print(avg)
#    return avg #return/store value in/to function3(x,y)

#x = int(input("enter value for x "))#x value is stored in a
#y = int(input("enter value for y "))#y value is stored in b
#v = function3(x,y)
#print(v)

"""doc string help us to know what function2 does
if we have 100 functions in code and we want to know what function does what ther we take the help of 
docstring to know . if we keep pressing ctrl key in keyboard and press in function3 we will know about function"""


""" _doc_  function . to print docstring """
#def function3(a,b):
#    """this line is docstring"""
#    avg = (a+b)/2
#    return avg
#v = function3(5,7)#user gave input
#print(v)
#print(function3.__doc__)#to print the docsting




'''           try except exception handling                   '''




"""suppose we are running a code which may or maynot show 
error   eg - """
#num1 = int(input("enter value for num1 : "))
#num2 = int(input("enter value for num2 : "))
#print(num1+num2)
"""if we take input for num1 as 6 and for num2 a string like dd ,then error will come.
suppose after first statement we have one more print statement an we want to execute it even if first 
print statement shows error
then we use 'try' keyword and 'except Exception as <variable name>' """
#num1 = input("enter value for num1 : ")
#num2 = input("enter value for num2 : ")
#try:
#    print(int(num1)+int(num2))

#except Exception as e:
#    print(e)

#print("rhis line is important")
""" 'try'  keyword wil try to execute the first print() if error will come,the error will be stored in
 variable in e and e will be printed,but 2nd print() will not be affected because of 1st print statement.
 don't use int with input()  error will come """






'''                   FILE HANDING IN PYTHON                '''






"""
a file is a resource for saving data and information in computer hardware .
a file is stored in form of bytes in hardware like in hard disk.

a file open in RAM but stored in hard disk because hard disk is 
non-volatile i.e;hard disk store information permanently but RAM is
volatile i.e;it store information temporarily ,it losses data soon
after computer is closed/shutdown.

in non-volatile we store things in form of file . it can contain
text,mp3,video,images etc...  .all these things we encode and store
it in one place in form of file . and the software like mp3 player,
window image viewer etc... decode the file or read each bit of data
in file and take the decision on how to present it to user.
"""




""" MODES IN WHICH A FILE CAN BE OPENED"""


"""
'r' - read mode.to read a file.it is default mode
't' - text mode.open file in text format.it is also default mode
'w' - write mode.open a file to write
'x' - create file if file does not exist before but if file exist before don't create
'a' - add more content file at the end/last
'b' - binary mode (discussed above)
'+' - plus mode update file.this is read & write mode
"""

"""HOW TO WRITE IN A FILE"""
"""AT FIRST CREATE A NEW TEXT FILE IN PYCHARM NAME ANYTHING LIKE 
AND WRITE SOMETHING LIKE


I AM DEMON KING
DEMON IS BACK
DEMON NEVER DIE 


"""

#open("textfile.txt")
"""output will not come bcz we need a file pointer"""


'''read()'''



"""to access a file we need a file pointer i.e;open().it point/return
a file and store it in variable f . read() helps to read the contents in file.
we should also close a file(it's not compulsory')because if we want to free all 
the resources we need to deal with file we need to close it by using cose(),
so that other person accessing the file will not face any error
"""
#f = open("textfile.txt")
#content = f.read()
#print(content)
#f.close()

'''if we will add r/t/rt(read/text/read and text)mode in open() 
no change will occur because r&t is default mode '''
#f = open("textfile.txt","r")
#content = f.read()
#print(content)
#f.close()

'''if we will add b (binary) then;   (don't use only b use rb)'''
#f = open("textfile.txt","rb")
#content = f.read()
#print(content)
#f.close()

'''if we will write 3 in read() then 6 characters i.e;upto length 6 will be printed'''
#f = open("textfile.txt","r")
#content = f.read(6)
#print(content)
#f.close()

'''if we will write 35 in read() then 35 characters/upto length 35 text will be printed '''
#f = open("textfile.txt","r")
#content = f.read(35)
#print(content)
#f.close()

'''if we write 6874 n read() then whole text will be printed '''
#f = open("textfile.txt","r")
#content = f.read(6874)
#print(content)
#f.close()


"""readline() """

'''readline() print only one line(line1 not line2,3,4...) in a file
if we print'''
#f = open("textfile.txt")
#c = f.readline()
#print(c)
#c = f.readline()
#print(c)
#c=f.readline()
#print(c)
"""
we are getting a blank space because by default print statement means new line and 
a new line after each sentence is already present .so we are getting a blank space.
if we want to remove the blank space then,use end statement
"""
#f = open("textfile.txt")
#c = f.readline()
#print(c , end = "&")
#c = f.readline()
#print(c, end= "")
#c=f.readline()
#print(c)

#or we can write this also

#f = open("textfile.txt")
#print(f.readline() , end = "&")
#print(f.readline() , end = " ")
#print(f.readline() , end="#")


"""we can also print line by line by as we print by using readine() by using 
 for in statement(for loop)"""
#f = open("textfile.txt")
#for line in f :#line is a variable which initalise index of elements in file & f store file
#    print(line, end="&")





'''WRITING AND APPENDING TO A FILE'''





"""write mode delete all previous data in file and print the new text but"""
#f = open("textfile.txt", "w")
#print(f.write("hy i am x "))
#f.close()

#f = open("textfile.txt", "w")
#print(f.write(5*"hy i am x \n"))
#f.close()

"""if we print a new file name in open() then a new file will be created"""
#f= open("newtext.txt","w")
#print(f.write("this is a new file"))
#f.close()

"""appending means to add a text in file,it add new words at end of a file
here also if we give a new file name a new file will be created"""
#f = open("textfile.txt","a")
#print(f.write("this is appending"))
#f.close()

"""open file in both read and write mode"""
#f = open("textfile.txt", "r+")
#print(f.read())
#print(f.write("this is r+ mode"))





'''     tell() in python     '''





""" 
tell() say where the file pointer is i.e;open()
if we add some more text in file like

bhai
more words

"""

#f = open("textfile.txt")
#print(f.tell())
#print(f.readline())
#print(f.tell())
#print(f.readline())
"""
output is
0
hy i am x 

12

here o says that index of 1st sentence start from 0
and 12 says that 2nd sentence start from index 12
"""





'''seek()'''
'''if i want to restart the file pointer(i.e;open()) then after printing 1st sentence
then i use seek()'''
#f = open("textfile.txt")
#print(f.tell())
#print(f.readline())

#print(f.seek(0))
#print(f.tell())
#print(f.readline(10))
"""after printing 1st sentence the pointer should move to 2nd sentence
but seek() again brought the file to index 0 
if i use seek() first then"""
#f = open("textfile.txt")
#print(f.seek(20))
#print(f.tell())
#print(f.readline())

#f.seek(12)
#print(f.tell())
#print(f.readline(1))




'''          OPENING FILES WITH BLOCK         '''




# with open("textfile.txt") as f:
#    print(f.read())
"""
instead of writing the above code as
as below we wrote using 'with' block

f = open("textfile.txt")

print(f.read())

with block does the work of both open() and close().
"""





'''      LOCAL AND GLOBAL VARIABLE AND THEIR SCOPE      '''



"""
global variables are the variables which are declared outside the function 
and can be used by any function
suppose we have made one function names function1 so,l=7 is global variable because
l=7 is declared outside the function1 and it can be used by any function in a 
program.if in a program there would be 100 functions all functions can use it i.e;l=7

local variables are the variables which are declared and can be used only 
inside function in a program.
l=10 and m=45 are local variable because they are declared inside function1(locally)
and they can only be used inside function1.if in a program there would be 100 
functions all functions can't use it only function1 can use it i.e;l=10 and m=45"""


#l=7 #this is global variable
#def function1():
#     l=10#this is local variable
#     m=45
#     print(l,m)
#
# function1()




"""            scope of local & global variable           """




"""if we print l outside function then l will be 7 not 10 but because
 l is in global scope. scope means how far l can go 

if we print l inside function
then l will be 10 bcz local variable can only be used inside function or
l is in local scope
"""
# l=7 #this is global variable
# def function1():
#     l=10#this is local variable
#
# function1()
#print(l)





'''   use of global keyword   '''





"""now if we want to add 10 to l we can't because global variable can not be changed,
so in order to change value of global variable we need to take permission from python.
so to take permission we have to use 'global' keyword"""

# l=7 #this is global variable
# def function1():
#     m=45
#     global l#we got permission to change global variable
#     l = l +10
#     print(l,m)
#
# function1()





'''nested function   (function inside function is nested function)'''





# def harry():
#     x = 10
#
#     def rohan():
#         global x
#         x=88
#
#     print("before calling rohan()",x)
#     rohan()
#     print("after calling rohan()",x)
# harry()
# print(x)
"""so here we can see that before and after calling rohan()
value of x is 10 instead of 88 an 10. here value of x doesnot in
before calling rohan()i.e;our expectation is 88 as x is declared globally
but result is 10 because when we declared x as global the control moved
outside both harry() and rohan() an search value of x outside both functions

but if we print x outside both functions i.e;below calling of harry()
then x will 88 as x is a global variable .in 'before calling rohan()' 
we got x as 10 because at that rohan() was inside harry() and there 
local value of x is 10 so rohan() also print x as 10 because
at that x first check for local variable and then for global variable"""



"""what if we declare x=90 globally then also output is 88"""
# x=90#global variable
# def harry():
#     x = 10
#
#     def rohan():
#         global x
#         x=88
#
#     print("before calling rohan()",x)
#     rohan()
#     print("after calling rohan()",x)
# harry()
# print(x)






'''    RECURSION   VS   ITERATION    '''

"""recursion means using a function inside function or
when a function call itself we call it recursion """


# def function1(str):
#     print("hello" + str)
# function1("bye")

"""here if we use one more function having name function1 then"""

# def print2(s):
#     print("demon "+s)
#     print2(s)
#
# print2("hello")

"""here we got error as (RecursionError: maximum recursion depth exceeded while calling a Python object).
because print2(s) is calling [def print2(s):] repetedly infinite times.so the system may hang.
by default it can print 1000 times but after some modification\customization it can print more than
but max is 4000 times.so this is called as recursion,i.e;a function call itself repetedly.

so we need to break the recursion"""










'''HOW TO USE RECURSION & DIFFERENCE BETWEEN RECURSION AND ITERATION'''


"""PRINT FACTORIAL OF A NUMBER"""

"""

eg - factoial of 5 are 1,2,3,4
     5*4*3*2*1=120 

by using ths logic
formulae = (n! = n* n-1 *n-2 *n-3 *n-4...to 1)
(n!)this sign we call as (n factorial)

if we can also write the above formulae as
n! = n* (n-1)!
(factorial of n is equal to n*(factorial of n-1))

(n-1)! represent n-1*n-2*n-3*n-4*....to 1


"""

# def factorialiterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#
#     return fac
# number = int(input("enter your number : "))
# print("calculate using factorial iterative method \n",factorialiterative(number))

"""we have calculated the factorial of a number with the help of iteration(loops) not reculsive

iteration is that in which we use loops,the loop continues until the condition
is fulfilled

if we want to calculate using reculsive then
"""

# def factorialreculsion(n):
#
#     if n == 1:
#         return 1
#
#     else:
#         return n*factorialreculsion(n-1)
#
# number = int(input("enter your number : "))
# print("calculate using factorial recursive method",factorialreculsion(number))
# print("calculate using factorial iterative method",factorialreculsion(number))

"""so we can see that output will same in both iterative and recursive method.

so logic is if n value is 1 then it will return 1.if not then
return n*(n-1)

eg - lets take n=5

return  n*factorial recursive(n-1)
        5*factorial recursive(4)  #5-1
        5*4*factorial recursive(3) #4-1
        5*4*3*factorial recursive(2) #3-1
        5*4*3*2*factorial recursive(1)  #2-1

when n=1 then control move to if statement and check if n==1,
the ans is yes,so the value of 1 in if condition will be replaced with 
5*4*3*factorial recusive(1)  #2-1


and last step will be
5*4*3*2*1factorial recursive(0)

"""







"""_______________________________________________________________________"""









"""USING PYTHON EXTERNALS AND BUILT IN MODULES"""




'''now at 1st lets try with random module'''

"""to know about random module press ctrl+right click"""
#import keyword is used to use any module like random
# import random

# random = random.randint(0,10)
#when import word's color change from grey to blue,means you are using random module

# print(random)
#in output any number between 0to10 can come including 0&10


"""after importing random module we can use submodules of random modules
or functions provided by random modules,like random(),randint() etc"""


"""use of random()"""
# import random
# rand = random.random()
# print(rand)


'''if we want random() to generate number between 0to100 then multiply 100'''
# import random
# rand = random.random() *100
# print(rand)


"""use of choice()  it select any name in list randomly"""

# list= ["star plus","sony tv","demon","ufc","ipl"]
#
# import random
# randchoice = random.choice(list)
# print(randchoice)



"""as a programmer you don't have to remember all fuctions or submodules of any module like random
you can search it in inernet any you can know how to use them"""









"""==========================================================================================="""










"""string formatting and f strings"""

"""string formatting means we can insert a variable inside a string
we can do that using 3 ways.
1st way of string formatting
"""

# me = "back"
# me2 = "the demon king is %s" %me  #'s' letter should small
# print(me2)

"""but here in 1st method of string formatting problem is 
if there are 100 variables like 'me' and we have insert all those 100 variables 
in 1 variables like 'me2' the program will be very complex"""



# me = "python"
# m2 = "3"
# m3 = "i am using python %s %s" %(me,m2)
# print(m3)





"""the method of string formatting is using dot(.) operator"""
# me = "harry"
# m2 = "3"
# m3 = "this is {} {}"
# a = m3.format(me,m2)
# print(a)


"""if in 1st curly bracket if i write 0 & in other as 1 then"""
# me = "harry"
# m2 = "3"
# m3 = "this is {0} {1}"
# a = m3.format(me,m2)
# print(a)
'''in above 'me' is stored in 1 and 'm2' is stored in 1'''
""" me's place is 0 and m2 place is 1
if we declare 1 and then 0 in 'm3' then 'm2' will print 1st then 'me' """


"""if in 1st curly bracket if i write 1 & in other as 0 then"""
# me = "harry"
# m2 = "3"
# m3 = "this is {1} {0}"
# a = m3.format(me,m2)
# print(a)
'''in above 1 store 'm2' and 0 store 'me' variable '''


# me = "harry"
# m2 = "3"
# m5 = 56
# m3 = "this is {1} {0} {2}"
# a = m3.format(me,m2,m5)
# print(a)
'''in above 1 store 'm2' and 0 store 'me' variable and 2 store 'm5' '''
""" me's place is 0 and m2 place is 1 and m5 place is 2
if we declare (1 then 0 and then 2)in 'm3' then 'm2' will print 1st then 'me' then 'm5' """

"""here is also same problem as above 
program becomes complex when there are 100 variables like(me & m2)
and we have to add them in 1 variable like 'm3' """




"""these 2 methods of file formatting can be replaced with 'f string' type of formatting"""

# f" " means this is a f string
# me = "harry"
# m2 = 3
# m3 = f"ths is {me} {m2}"
# print(m3)

#if we add {6*5} in m3 then
# me = "harry"
# m2 = 3
# m3 = f"ths is {me} {m2} {6*5}"
# print(m3)


'''we can import math functions in f string'''
# import math
# me = "harry"
# m2 = 3
# m3 = f"ths is {me} {m2} {6*5} {math.cos(65)}"
# print(m3)











"""--------------------------------------------------------------------"""












'''*args and **kwargs functions in python '''







# def funargs(a,b,c):
#     print(a,b,c)
# funargs("harry","rohan","hammad")#calling funargs()

"""in above we have created a funargs() that take 3 arguments.
no if we want to add vikas in the list then we have to add one more arguments as 
'd' then call hammad like below

def funargs(a,b,c,d):
    print(a,b,c)
funargs("harry","rohan","hammad","vikas")#calling funargs()


but if we want make a scalable application where millions of user were added daily
like in facebook or twitter then we cannot do that as we did above 
i.e;adding argument to print new names. so we use *args 
"""






# def funargas(*ars):
#     print(type(ars))
#     print(*ars)
# funargas("harry","rohan","hammad","vikas")

""" here if we want add new names like vikas then we don't have to add new arguments 
as we did earlier.we only have to write name of vikas in calling function i.e;funargs()
the names are stored in form of tuples,we can see it using type().







we can also use list """

# def funargas(*args):
#     print(type(args))
#     print(*args)
#
# list = ["harry","rohan","hammad","vikas"]
# funargas(*list)

'''here (*)multiplication sign is necessary not name after it we can also give other name like *funs
so the list is called by [ funargs()']  and it is stored in
[ def funargas(*ars): ] in form of tuple only not in form of list or set etc and *args is printed.
if we remove * sign in print statement and write it as ' print(args) ' ,
then name will be printed inside of tuple.'''






"""we can also use for loop here"""
# def funargas(*fun):
#     print(type(fun))
#     for items in fun:
#         print(items)
#
# list = ["harry","rohan","hammad","vikas","demon"]
# funargas(*list)
"""if we add demon then it will also be printed.if we will write 100 names then they all will also be printed
this is the advantage of *args. we don't have to add more arguments to insert new names"""





'''we can also insert normal values like int,string etc'''
# def funargas(normal,*argsfun):
#     print(normal)
#     for items in argsfun:
#         print(items)
#
# list = ["harry","rohan","hammad","vikas","demon"]
# normal = "this is a normal string"
# funargas(normal,*list)

"""so in above we have take argument of normal first then *args then **kwargs. if we take *args first then normal value 
output will be error.
if in calling function if call list first then normal,list will he printed first then string stored in normal
example - """
# def funargas(normal,*argsfun):#dont call *args 1st then normal error will come
#     print(normal)
#     for items in argsfun:
#         print(items)
#
# list = ["harry","rohan","hammad","vikas","demon"]
# normal = "this is a normal value"
# funargas(*list,normal)#1st list will be displayed then string



"""**kwargs in python"""

# def funargas(normal,*argsfun,**kwargs):
#     print(normal)
#     for items in argsfun:
#         print(items)
#     for i in kwargs:
#         print(i)
#
# list = ["harry","rohan","hammad","vikas","demon"]
# dict = {"rohit":"fish","sonu":"egg"}
# normal = "this is a normal value"
# funargas(*list,normal,**dict)#1st list will be displayed then string then dict

"""here also we have take normal argument 1st then *args then **kwargs as per rule
in calling function place i.e; we can declare any one first except **kwargs as per rule.
if list will be called first it will print 1st or if normal will be declared 1st,it will print 1st
but nothing can be called after **kwargs as per rule"""




"""we can also use f-string here"""
# def funargas(normal,i,*argsfun,**kwargsfun):
#     print(normal)
#     for items in argsfun:
#         print(items)
#     print("introduction to **kwargs \n")
#     for key,value in kwargsfun.items():
#         print(f"{key} loves to eat {value}")
#
# list = ["harry","rohan","demon\n" ]
# dict = {"rohit":"fish","sonu":"egg","demon":"flesh\n"}
# normal = "this is a normal value \n"
# i = 5*5
# funargas(*list,normal,i,**dict)#nothing can be declared after **kwargs





"""time module in python"""


# i=0
# while i<45:
#     print("this is a loop")
#     i=i+1
#
#
# for i in range(45):
#     print("this is a loop")

"""so here there are 2 loop one in while loop and other is for loop.
now i want to know which loop takes less time to finish execution i.e;to print 'this is a loop' 
45 times. so i can know by using time module """

# import time
# initial = time.time()
# print(initial)
#
# i=0
# while i<45:
#     print("this is a loop")
#     i=i+1
#
#
# for i in range(45):
#     print("this is a loop")

"""
1st - so here first we have imported time module

2nd - then we have used time function which was inside time module and stores it in initial
      time() gives no of 'ticks' ,1 tick = 1sec . 


in output we can see that a number would have been printed like ' 1601526304.2389736 ' ,
this is time which give from milli second


now if i want to print the time taken by while and for loop individually then
"""



# import time
# initial = time.time()
#
# i=0
# while i<4555:
#     print("this is hARRY")
#     i = i+1
#
# print(f"while loop ran in {time.time() - initial} milli seconds")
#
#
# initial2 = time.time()#restart the again
#
# for i in range(4555):
#     print("this is harry")
#
# print("for loop ran in", time.time() - initial2 , "milli second")

"""
SO HERE
1st - we have imported time module

2nd - we have used the time() which was inside time module. (.)dot operator help to access
time()[ time.time() ] . the time.time() returned/store a time to/in initial

3rd - we did our work in while loop.

4th - when control moves out of while loop,we subracted the 2nd time.time() under while loop
with initial 
           
            time.time()-initial
            (new time) -(old time)

after that in output we can see how much time did while loop took finish its execution


----------------------------------------------------------------------------------------------


5th - then we again restarted time or we built another time() for 'for loop'.
       so now we stored the new time in variable initial2                  

6th - we runned the for loop ,after for loop finished its execution
        control comes down and then we subtracted 2nd time.time() with initial2

                    time.time()-initial2
                    (new time) -(old time)

after that in output we can see how much time did while loop took finish its execution

"""


"""the time module is very big . so we don't have remember all functions of time module,
we can search it in internet"""



"""lets do something more with time module"""
# import time
# local_time = time.asctime(time.localtime(time.time()))
# print(local_time)

"""in above time.time() is optional.
so time.localtime() convert time.time() in local time.this function takes 2 parameter
and returns date and time in time.struct_time format.
and then time.asctime converts tuple into presentable time format which is in output
"""


"""time.sleep()"""
"""it stop the execution for limited second and again start then stop again and it goes on"""
# import time
# for i in range(5):
#     print("return of demon kings")
#     time.sleep(2)#stop execution for 2 second









'''----------------------------------------------------------------------------'''










"""enemurate functions in java"""






"""now think that we have a list named l1.
now if i want to print only "blood and water"&"eminem" """

#l1 = ["blood and water","hall of fame","eminem","not afraid"]

# i=0
# for z in l1:
#     if i%2==0:
#         print(z)
#     i+=1


"""this process can be shorten using enemurate function
.it gives both index and item of list"""

l1 = ["blood and water","hall of fame","eminem","not afraid"]

# for index,items in enumerate(l1):
#     # print(index,items)
#     if index%2==0:
#         print(items)

"""here index stores index of elements of list which start from 0 and 
items store elements of list."""










"""------------------------------------------------------------------------"""









"""   usage and necesity of    if __name__ == '__main__':     """







"""
now at first create a 2 python file named like 'practice program.py' and 'program.py'

afterwards create 2 functions.first function take a string and return.
2nd function take to argument to add,but gives wrong output 
"""

# def mainharry(string):
#     return f"give this string to bro {string}"
#
# def add(num1,num2):
#     return num1+num2


"""
after that in practice program.py file import program
use add use add function to print addition of 6&4

import program
print(program.add(4,6))

you will get the output as 10

----------------------------------

but if we have wrote some test codes to test the functions.like below
"""
# print(mainharry("harry"))
#
# print(add(5,2))

"""
now if we compile in ' practice program.py ' file then 
the output will be - 

give this string to bro harry
7
10

but our output should be only 10 ano that 7 and string
this is happening because when we imported program file in practice program.py file
it execute all content present in program file .

to stop the execution other things
we have to use main function(if __name__ == '__main__':)

"""

# def mainharry(string):
#     return f"give this string to bro {string}"
#
# def add(num1,num2):
#     return num1+num2
#
#
# if __name__ == '__main__':
#
#
#     print(mainharry("harrry"))
#     print(add(5,2))


"""
now if we run the code in practice program.py we will get the correct output as 10
other things will not be displayed like it happened before using main function.

this happens because when contents in main function will not be executed
outside even if we have imported as we did here 
if we compile it in program file(where we wrote main function) 
contents inside main function will be executed but if we compile
in practice program.py main function will not be .
this is the advantage of main function(if __name__ == '__main__':)

"""





"""use of join() in python"""






"""we have a list and we want to print output like (demon and king and barlor and club ) """

# list = ["demon" , "king" , "barlor" , "club"]
# for item in list:
#     print(item , "and" ,end = " ")

"""this whole process can eliminated using join()"""
# list = ["demon" , "king" , "barlor" , "club"]
# a = " and " . join(list)
# print(a)

"""we can also give comma (,) in place of and"""
# list = ["demon" , "king" , "barlor" , "club"]
# a = " is " . join(list)
# print(a)



'''---------------------------------------------------------'''




"""use of map()"""



# list = ["2","3","4","5"]

# for i in range(len(list)):
#     list[i] = int(list[i])
#
# list[1] = list[1]+5
# print(list[1])

"""
suppose we have a list and where some numbers are stored in form of string.
now if i want to add 5 to any number in list (stored in form of string) at first i have to 
convert all elements of list into int. bcz 5 cannot be added to a string 

but this process can be reduced using map() 
"""


'''map()'''



# num = ["2","3","4","5"]
#
# ##print(map(int,numbers))
# list = list(map(int,num))
# '''int represent to what you want to convert and num represent what you want to convert into int'''
#
# list[2] = list[2] + 5
# print(list[2])

"""

so this is an example of map function.
so what we did above is at first map() is converted to list
because map() returns object.
map() converts all elements in list into int and stored in list variable
if you will write [ print(map(int,numbers)) ] 
and then run the code you will get a output
as ' <map object at 0x007B1FE8> ' .it shows that 
map returns object and it is stored in (0x007B1FE8)
"""



"""we can also use lamda() with map()"""

# def add(a,b):
#     return add(a,b)
"""
this thing can be replaced using lambda() like
lambda a,b: add(a,b)
"""

# num = [2,3,5,6]
# add = list(map(lambda a : a*a  , num))
# print(add)



"""we can also print do something more"""
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# fanc = [square,cube]
#
# for i in range(5):
#     val = list(map(lambda x:x(i) , fanc))
#     print(val)
"""
here what happened is at first we create two function
to square number and other to cube a number
then we store both square and cube in one place like
( fanc = [square,cube] ) . and teh we create a lambda function that take argument as x
and return x(i) i.e;return x as well as fanc (fanc = [square,cube])

example - 
if in x we gave square of 1.and
if i=1 , it returns square of i .i start from 0



as i represent fanc and fanc=[square,cube]
so at first it will print
[square of i,cube of i] i.e;[0, 0] here i=0. then
[square of 1,cube of 1] i.e;[1, 1] then
[square of 2,cube of 2] i.e;[4, 8]
it continue to 4 as range is upto 4
"""








'''------------------------------------------------------'''







"""filter()"""

"""suppose we have list that contain some numbers but we want to print only 
the numbers that are greater than 5"""

# num = [5,6,7,3,12,6,4,9]
# greater = list(filter(lambda a : a>5 , num))
# print(greater)

"""so here also filter() returns object as map(),so we convert filter() into list.
and also take arguments as map()"""



"""reduce()"""


"""suppose we have a list and want to print sum of all sum
in a list i.e;2+3+4
"""

# num = [2,3,4]
# from functools import reduce
# num = reduce(lambda a,b : a+b , num)
# print(num)

"""so at first 2 is added to 3 and then addition of 2 and 3 is added to 4
                2+3 = 5
                5+4 = 9
"""






"""              decorators in python                  """

# def function1():
#     print("this is nothing")
#
# func2 = function1
# func2()

"""if i delete function1 after storing it in func2.then also output will be displayed 
because elements of function1 is stored in func2 already"""
# def function1():
#     print("this is nothing")
#
# func2 = function1
# del function
# func2()


"""now how to use a function within a function(how to return a function through function)"""
# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1 :
#         return sum
#
# a= funcret(0)#calling funcret
# print(a)

"""
here when we gave 0 in calling funcret output
came is ' <built-in function print> ' here
we can know that print is a built in function
i.e;    if num == 0:
        return print
this is a built in function and sum is also a function.
this is how a function return function

when we return sum 'sum' was stored in 'a'
"""




'''we can also give function as as argument'''
# def executor(a):
#     print("this")
#
# executor(print)#print function is given as an argument
"""here we gave print function as an argument """




"""decorator concept """


"""upto this we are revising some things about functions .
because we need those here while doing decorator in function"""



# def dec(func):
#     def innerdec():
#         print("executing code")
#         func()
#         print("code executed")
#     return innerdec
#
# def harry():
#     print("harry")
# harry()
"""when we compile 'harry' came in output"""









"""but if we store harry in dec or if we give harry function as argument in dec()then output will be

output      executing code
            harry
            code executed 
"""
# def dec(func):
#     def innerdec():
#         print("executing code")
#         func()
#         print("code executed")
#     return innerdec
#
# def harry():
#     print("this is me")
# harry = dec(harry)
# harry()
"""
so here when we stored 'harry' in dec() harry() is not harry i.e;harry()
will not print 'this is me' now it is that hat dec() return.

in simple words 'this is me' is stored in dec().
now after that control comes down to innerdec() and 1st it will print
'executing code', then as func() is called so it will print 'this is me',
and after that it will print 'code executed'. 


now instead of writing 'harry=dec(harry)',we can write '@dec' before 'def harry()'.like below
"""
# def dec(func):
#     def innerdec():
#         print("executing code")
#         func()
#         print("code executed")
#     return innerdec
#
# @dec  #shortcut sign
# def harry():
#     print("this is me")
# harry()



















"""                     OOP CONCEPT IN PYTHON                            """
"""----------------------------------------------------------------------"""


















"""classes and objects in python"""


"""class is a collection of objects and objects are templates of class"""









'''writing our 1st class in python'''






# class student :
#     pass
#
# harry = student()
# rohan = student()
# print(harry,rohan)

"""so here we have created class named student and harry and rohan are its object.
when we print harry and rohan in output we saw that 
harry and rohan's location came . (<__main__.student object at 0x00E61FD0>, 
<__main__.student object at 0x00E7B028>) 1st one is of harry's and other is of rohan
in output e can see that it is written 'student object' which means both 
are are objects of class student and then location is printed . both have different location.
it means  harry and rohan are two different objects of same class .
"""










"""instance and class variable"""








# class student:
#     pass
#
# harry = student()
# rohan = student()
#
# harry.name = "Harry"
# harry.std = 7
# harry.section = "A"
#
# rohan.name = "Rohan"
# rohan.std = 8
# rohan.section = "B"
#
# print(harry.name)
# print(harry.std ,"," ,rohan.section)
#
"""
so harry.name ,rohan.name , harry.std = 7 etc...  . these all are
instance variable,which stores somes value . 
we can access or print the value stored in instance variable by
printing the name of instance variable i.e;print(harry.name)
or print(harry.std ,"," ,rohan.section).
"""



# class employment:
#     no_of_leave = 10
#     pass
#
# harry = employment()
# rohan = employment()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.section = "programmer"
#
# rohan.name = "Rohan"
# rohan.salary = 855
# rohan.role = "accountant"
#
#
# print(harry.salary ,"," ,rohan.salary)
#
# print(rohan.no_of_leave)
# print(harry.no_of_leave )

"""so here harry and rohan are two employees.harry and rohan's salary 
are their private property.other employees can't access harry and rohan's
personal information.
but no_of_leaves is a public property or class variable.all objects of class can
access/share it,like harry and rohan.but objects outside class employee can't access it
i.e;no_of _leaves . no_of_leave neither belongs to harry nor rohan,it belongs to
class employee .all objects of class employee can access it,but can't change.
no_of_leave is same for all objects

we can also access no_of_leave through class employment like below
"""
# print(employment.no_of_leave)







"""How to change class variable"""




"""if we want to change class variable we can change it only through class employement"""
# class employment:
#     no_of_leave = 10
#     pass
#
# harry = employment()
# rohan = employment()
#
# harry.name = "Harry"
# rohan.name = "Rohan"
#
# print(employment.no_of_leave)
#
# employment.no_of_leave = 9#value of class variable changed to 9
# print(employment.no_of_leave)

"""so above you can see that at first when we print class variable 
i.e;print(employment.no_of_leave)
value of no_of_leaves was 10 .but after that when we made one more instance of 
class employment i.e;employment.no_of_leave = 9 
and store value of no_of_leave as 9 .and after that when we print 
class variable , value of no_of_leave was 9


but harry or rohan can't change it.then can only access it like below
"""
# class employment:
#     no_of_leave = 10
#
# harry = employment()
# rohan = employment()
#
# harry.name = "Harry"
# rohan.name = "Rohan"
#
# print(employment.no_of_leave)
#
# rohan.no_of_leave = 9#value of class variable changed to 9
# print(rohan.no_of_leave)
"""when we tried to change change class variable i.e;no_of_leave , then
a new instance variable was created storing 9.now it belongs to rohan only.
to verify that we can take help of  _dict_   function"""


"""use of _dict_"""

"""it returns a dictionary like below"""

# class employment:
#     no_of_leave = 10
#
# harry = employment()
# rohan = employment()
#
# harry.name = "Harry"
# rohan.name = "Rohan"
#
# rohan.no_of_leave = 9#value of class variable changed to 9
# print(rohan.__dict__)
#
# employment.no_of_leave=5
# print(employment.__dict__)

"""
so output is -
{'name': 'Rohan', 'no_of_leave': 9}

we can see that no_of_leave is 9 not 10
"""












"""-------------------------------------------------"""











"""self   &  _init_()/constructor"""










"""self"""

# class employment:
#     no_of_leave = 10
#
#
#     def printdetails(self):
#         return f"my name is {self.name} and my salary is {self.salary} " \
#         f"and my role is {self.role}"
#
#     # """in above 'self' means that object in which the function will act.
#     # if i run the function with rohan like 'print(rohan.printdetails())'
#     # then rohan object will be stored in self."""
#
#
#
# harry = employment()
# rohan = employment()
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "programmer"
#
# rohan.name = "Rohan"
# rohan.salary = 855
# rohan.role = "accountant"
#
# print(rohan.printdetails())
#

"""by seeing the output we may think that we did not give anything
in details  like ' (rohan.printdetails( 'name or role' )) '
but then also we are able to access the instance of rohan .

it happens because rohan object including all its instances were stored in 
'self' automatically just by writing 'print(rohan.printdetails())'.
that's the beauty of methods."""




"""
def printdetails():
    return f"my name is {self.name} and my salary is {self.salary} " \
    f"and my role is {self.role} "


if we remove self like above and leave that place blank then error will come
and a message would be written like below at last.

' TypeError: printdetails() takes 0 positional arguments but 1 was given '

in error it was written that 'takes 0 positional arguments but 1 was given ' that means 
rohan was already went to argument place as soon as the function was made even if 
we had not given any argument like 'self' .that's why it was written takes 0 position .

to handle rohan object we gave one argument as 'self' .
this is convection in  python OOP . if we had wrote 
' print(harry.printdetails()) ' then output would be 

'my name is Harry and my salary is 455 and my role is programmer' 

all these things we can also do normally but 00P
makes them more organized
"""







"""_init_(self) or constuctor"""








"""when we made a employment object like rohan.
instances of object we have to write manually like below

rohan = employment()
rohan.name = "Rohan"
rohan.salary = 855
rohan.role = "accountant"


now if we want something like we can give argument to
employment() like 'harry=employment("harry",455,"instructor")',
so that we do not have to write all the instance variable manually. 


if we want to give argument to employee() then we have to
take the help of constructor/_init_(self)
"""



# class employment:
#     no_of_leave = 10
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.arole = arole
#
# harry = employment("harry" , 455 , "instructor")
# rohan = employment("rohan" , 4551 , "instructor")
#
# print(harry.salary)

# this is the function of constructor.it construct automatically.
# it do all the work we want to do during making
# if objects . in 'self' harry object is stored and in 'aname' harry is stored and 455 is stored
# 'asalary' automatically.we dont have create the instance variable like
# we did before.constructor create automatically
# harry,455 and instructor are stored in  _init_








"""              CLASS METHOD             """







"""now think how to change class variable.
earlier we discussed that a class variable can only be changed
through class employee like 'employee.no_of_leave=8' 

but now if want to change class variable through function and
i don't want to use 'self' method as it decrease the efficiency of program"""
# class employee:
#     no_of_leave = 10
#
#     @classmethod #it is a decorator
#     def change_leave(cls,new_leave):
#         cls.no_of_leave = new_leave
#
# harry = employee()
# rohan = employee()
#
# harry.change_leave(45)#value of no_of_leave changed to 45
# print(harry.no_of_leave)

"""so like self method there is also a class method and it is written like this
'@classmethod'. it is a decorator & it can be applied to any method of class.
we can change value of variables using this method too.

after that we had made a function named as change_leave
it takes class (cls) as argument .cls represent that class whose 
instance is that object in which we want to apply like harry.
in simple words cls store employee class and its object is harry ."""






"""  how to use class method as an alternative method   """


# class employee:
#     no_of_leave = 10
#
#     def __init__(self,aname,asalry,arole):
#         self.name =aname
#         self.salary =asalry
#         self.role =arole
#
# harry = employee("harry",4550,"instructor")
# print(harry.role)


"""now suppose there is employee whose instance is written like below
karan = employee("karan-4551-student")
and i want that this string will break where dash(-) sign is given
and karan ,4551 and student would become 3 different instance variable automatically
by constructor . an when i write  'print(karan.salary)' an output would be 4551
"""


# class employee:
#     no_of_leave = 10
#
#     def __init__(self,aname,asalry,arole):
#             self.name =aname
#             self.salary =asalry
#             self.role =arole
#
#     @classmethod
#     def from_dash(cls,str):
#         param = str.split("-")
#         print(param)
#         return cls(param[0],param[1],param[2])
#
#
# karan =employee.from_dash("karan-4551-student")
#
# print(karan.name)


"""what we did above is we created a class method '@classmethod' 
then created a function named from_ash . it take cls which represent
class employee and it's object and instances.
then we split the string "karan-4551-student" into
karan,4551 & student using split().split("-") break the string where
dash(-) sign is given and result is in form of list like ['karan', '4551', 'student']
stored it in param.
then we pased the parameter to constructor using index number of list
karan index no is 0,4551 index is 1 and student index is 2



this is how we use class method as a constructor but default
constructor is _init_(self)


this alternative constructor is useful when have to deal with files containing
string data seperated by a seperators"""




"""we can shorten that like"""
# class employee:
#     no_of_leave = 10
#
#     def __init__(self,aname,asalry,arole):
#             self.name =aname
#             self.salary =asalry
#             self.role =arole
#
#     @classmethod
#     def from_dash(cls,str):
#         return cls(*str.split("-"))
#
# karan =employee.from_dash("karan-4551-student")
#
# print(karan.role)
"""at first we split the string where dash(-) sign is given
and then we used  star sign(*) with string so that argument will be passed
to cls which represent employee. then return statement return a object to 
karan and store it there in karan
"""






"""              STATIC METHOD             """


"""
now if we want to take a simple/normal method neither 'self' nor 'cls'.
normal method means neither i want to access instance variable nor class variable.
it should only keep in class,neither access nor change any class or instance variable.

like we want a such method that only print something 'i am good'.and store it in class.
for this we will make static method. like class method we have to make static method through
decorator i.e;@staticmethod


"""


# class employee:
#     no_of_leaves = 12
#
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#
#     @classmethod
#     def from_str(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def print_harry(string):
#         print("i am good" + string)
#         return 555
#
#
# harry = employee("harry",455,"investor")
# karan = employee.from_str("karan-565-student")
#
#
#
# print(karan.print_harry(" harry "))
#
# karan.print_harry(" print ")
# #555 is not printed but it is stored in karan.print_harry()
#
# print(harry.print_harry(" boy \n"))

"""in above return statement is not compulsory
when we used return statement 555 is stored in
'karan.print_harry()' and print() print both 555
and 'i am good harry'.if we remove 555 from
return statement then none will come instead of 555
because nothing is returned to print karan.print_harry()
"""







"""            single inheritance and example              """






"""suppose your mother is good at maths,so you are too good at maths.
that means you inherited the qualities of your mother . in sames way
in computer inheritance means a new class can copy/acquire the property
of an older or parent class,like functions,constuctors,objects,methods and everything
EXAMPLE - """


# class employee:
#     no_of_leaves = 12
#
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#             return f"my name is {self.name} and my salary is {self.salary} " \
#             f"and my role is {self.role}"
#
#     @classmethod
#     def from_str(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def print_harry(string):
#         print("i am good" + string)
#
#
# # single inheritance
# class player(employee):
#     #player class has copied\aquired all property of employee class
#     #you can add more functions & methods in player class
#
#
#     def __init__(self,name,ehobby,language,esalary):
#         self.name= name
#         self.ehobby = ehobby
#         self.language = language
#         self.esalary = esalary
#
#     def print_subham(self):
#         return f"my name is {self.name},hobby is {self.ehobby},language {self.language}," \
#                f"salary is {self.esalary}"
#
#     def print (self):
#         return f"my name is {self.name},salary is {self.salary},play {self.role}"
#
#
#
#
# harry = employee("harry",455,"investor")
# karan = employee.from_str("karan-565-student")
# subham = player("subham","SINGING",["C++","PYTHON"],5995)



# print(harry.printdetails())

# print(karan.role)
# karan.print_harry(" best friend")
# #print() is not used bcz there is no return saement
#
# print(harry.salary)
# harry.print_harry("boy")
#
# print(subham.print_subham())
#

"""we have created a class player which contains all property of
class employee.and after that we added a constructor and 2 functions.

this is the one moe propety of OOP which increase code reusability
to copy the functions of class employee in player class we can also use
copy paste method i.e;copy all properties from class employee
and paste it in player class.but it makes the code long and decrease
efficiency.so concept of OOP increase code reusability"""







"""                MULTIPLE INHERITANCE                """







"""this is also a type og inheritance
in single inheritance we can inherit only one class but 
in multiple inheritance we can inherit more than one class"""
# class employee:
#     no_of_leaves = 12
#
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#             return f"my name is {self.name} and my salary is {self.salary} " \
#             f"and my role is {self.role}"
#
#     @classmethod
#     def from_str(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def print_harry(string):
#         print("i am good" + string)
#
#
# class player:
#
#     def __init__(self,name,ehobby,language,esalary):
#         self.name= name
#         self.ehobby = ehobby
#         self.language = language
#         self.esalary = esalary
#
#     def print_subham(self):
#         return f"my name is {self.name},hobby is {self.ehobby},language {self.language}," \
#                f"salary is {self.esalary}"
#
#
# #multiple inheritance
# class cool_programmer(employee,player):
#     """cool_programmer has copied/acquired all properties of
#     both employee and player class.here order is important .
#     we can also add more more functions/methods in cool_programmer
#     """
#     def __init__(self,name,salary,role,language):
#         self.name=name
#         self.salary=salary
#         self.role=role
#         self.language=language
#
#     def print_mohit(self):
#         return f"mu name is {self.name},salary is {self.salary}" \
#         f"role is {self.role},language is {self.language}"
#
# mohit = cool_programmer("mohit",5566,"programmer",["c++","python","java"])
#
# harry = employee("harry",455,"investor")
# karan = employee.from_str("karan-565-student")
# subham = player("subham","SINGING",["C++","PYTHON"],5995)
#
# print(mohit.language)
#
# a=mohit.print_mohit()
# print(a)










"""MULTI LEVEL INHERITANCE IN PYTHON + EXAMPLE"""


# class dad:
#     pass
#
# class son(dad):
#     pass
#
# class grandson(son):
#     pass

"""this is an example of multilevel inheritance.
son inherit dad class and then grandson inherit son class.
in simple words grandson has copied/acquired all properties of
both son and dad class bcz son has acquired all properties of dad class
and then grandson acquired all properties of son class,it means grandson
has acquired all properties of both son and grandson class."""


# class dad:
#     baskeball = 5
#
# class son(dad):
#     dance = 1
#     def dance_plus(self):
#         return f"number of dance is {self.dance}"
#
#
# class grandson(son):
#     dance = 3
#
#     def dance_plus(self):
#         return f"oh yeah ! number of dance is {self.dance}"
#
# barlor =dad()
# harry =son()
# demon =grandson()
#
# print(demon.dance_plus())

"""
as we can see above that,in son class we made a variable named 'dance'
which store value as 1.and then we made a function which return 
number of dance is 1 
but when we did the same thing in grandson class but here we store
the value as dance as 3. then we create 3 object
barlor,harry & demon. then we called 'demon.dance_plus' output cames as
'oh yeah ! number of dance is 3',so the dance_plus() in son class has been
replaced with the dance_plus() in grandson class.our old dance_plus() was
overridden by new dance_plus() in grandson class.
"""








"""         ACCESS SPECIFIERS AND NAME MANGLING IN PYTHON            """







"""ACCESS SPECIFIERS PREVENT ACCESS OR SPECIFY ACCESS of class
.it is of 3 types - public,private,protected"""


"""
public access modifier   -   in public all function,variable,methods can be
used publicly.i.e;every other class can use it.public member are generally
declared in a class that is accessible by all other outside class.so all 
classes by default are public classes.up to now we have made public class

protected access specifier   -  in case of protected class,only its function
or subclass or child class can only access it but outside class can't access it.



example ---suppose you had a poster and it contain some information.now if you
want that everybody in your society can see it,we have to stick it outside our
house.this is called as public in oop.

but if you want that only your family members can see the poster,then you have
to stick it in inside your house.this is called protected in oop. 

but of want that only you can see not even your family,then your have to stick it
in your personal room.this is called as private in oop

"""

# class employee:
#     no_of_leaves = 10#this is public
#
#     _protected = 5#protected variable
#
#     __private = 2#private variable
#
#     def __init__(self,name,salary,passion):
#         self.name = name
#         self.salary = salary
#         self.passion = passion
#
#     def printdetails(self):
#         return f"my name is {self.name},salary is {self.salary}," \
#                f"passion is {self.passion}"
#
#     @classmethod
#     def change_leave(cls,new_leave):
#         cls.no_of_leaves=new_leave
#
# empl = employee("harry",5565,"programmer")
#
#
# print(empl._protected)
# print(empl._employee__private)

"""so protected variable can only be accessed by employee class 
and its sub classes or child class.

in order to print private variable we cant access directly as we accessed
protected variable like this - 'print(empl.__private)',error will come.
to access it we have to write it like this - 'print(empl._employee__private)'
because '__private=2' 2 is not only declared private but also python has made
it 'name mangeling',means we cant access it directly as we access private and 
public variable.to access we have to write like this  - 
'print(empl._employee__private)'. python has made its syntax complex so that
we may not use it outside mistakely.this propety is called name mangeling"""









"""            polymorphism          """
"""this is a concept means ability take various faces.example-"""

#print(5+6)
# print("5" + "6")

"""as you can see above when we print 5+6 output came as 11
but when we made 5 and 6 as string then print "5"+"6" 
output cames as 56 python took 5 and 6 as string then joined it
this property is called polymorphism."""








'''           overriding and super in python                   '''


#these 2 are done to achieve polymorphism

# class A:
#     classvar_a = "i am a class variable in class A"
#     def __init__(self):
#         self.var1 = "i am inside class A's constuctor"
#
#
# class B(A):
#     classvar2 = "i am in class B man!YEAH"
#
# a=A()
# b=B()
# print(b.classvar_a)

"""there is nothing new in above program.  now if we make
a instance variable named classvar_a then call"""
# class A:
#     classvar_a = "i am a class variable in class A"
#     def __init__(self):
#         self.var1 = "i am inside class A's constuctor"
#         self.classvar_a = "this is instance var in classA"
#
# class B(A):
#     classvar2 = "i am in class B man!YEAH"
#
# a=A()
# b=B()
# print(b.classvar_a)
"""we can see that instance variable is printed not class variable
because class B will first search for instance variable,so
"this is instance var in classA" is printed not 
"i am a class variable in class A".


so what happened above is,when we write classvar_a in B'S instance
like 'print(b.classvar_a)' ,then 1st print() will search classvar_a
in class B and search if there any instance variable is present.
as there is no instance variable so control move to class A which
was inherited ,then it will search there as there it is present
' self.classvar_a = "this is instance var in classA" '  ,so it
will print tht but if will overwrite then,
"""


# class A:
#     classvar1 = "i am a class variable in class A"
#     def __init__(self):
#         self.var1 = "i am inside class A's constuctor"
#         self.classvar_a = "this is instance var in classA"
#
# class B(A):
#     #varible is overwritten
#     classvar1 = "i am in class B man!YEAH,this is also overwritten\n"
#
#     #constructor is overwritten
#     def __init__(self):
#         self.var1="var1 is overWritten in class B\n"
#         self.classvar_a="now instance variable is overwritten IN CLASS B\n"
#         self.name= "demon king FINN BARLOR\n"
#
# a=A()
# b=B()
# print(b.classvar_a)
# print(b.var1)
# print(b.classvar1)
# print(b.name)

"""if you will remove classvar1 of class B then
variable of class A il be printed 
i.e;"i am a class variable in class A" 
but you cant remove from constructor and then call
like you will remove 'self.var1' from class B constructor
and then call,you will get an error because we have overwritten
the whole constructor now we can add or remove or change anything
in constructor"""







"""use of super()"""
# class A:
#     classvar1 = "i am a class variable in class A"
#     def __init__(self):
#         self.var1 = "i am inside class A's constuctor"
#         self.classvar_a = "this is instance var in classA"
#         self.special = "special string"
#
# class B(A):
#     #varible is overwritten
#     classvar1 = "i am in class B man!YEAH,this is also overwritten\n"
#
#     #constructor is overwritten
#     def __init__(self):
#         self.var1="var1 is overWritten in class B\n"
#         self.classvar_a="now instance variable is overwritten IN CLASS B\n"
#
# a=A()
# b=B()


"""suppose in class A's constructor we have made a special named variable
and we want to run it but we have not declared it in class B's constructor
we want to run that statement i.e;"special string",but we cant because
class A's constructor is overwritten and we have not declared it.
so we want a such constructor that run bot constructor of class A&B

in simple words if some variable will not present in class B but present in
class A then class A's variable will be printed like below.

to do this we take the help of super() like below"""

# class A:
#     classvar1 = "i am a class variable in class A"
#     def __init__(self):
#         self.var1 = "i am inside class A's constuctor"
#         self.classvar_a = "this is instance var in classA"
#         self.special = "special string"
#
# class B(A):
#     #varible is overwritten
#     classvar1 = "i am in class B man!YEAH,this is also overwritten\n"
#
#     #constructor is overwritten
#     def __init__(self):
#         super().__init__()
#         self.var1="var1 is overWritten in class B"
#         self.classvar_a="now instance variable is overwritten IN CLASS B\n"
#
# a=A()
# b=B()
#
# print(b.special)
#
# print(b.special,',',b.var1,',',b.classvar_a)




"""but if we write super() at last then"""


# class A:
#     classvar1 = "i am a class variable in class A"
#     def __init__(self):
#         self.var1 = "i am inside class A's constuctor"
#         self.classvar_a = "this is instance var in classA"
#         self.special = "special string"
#
# class B(A):
#     #varible is overwritten
#     classvar1 = "i am in class B man!YEAH,this is also overwritten\n"
#
#     #constructor is overwritten
#     def __init__(self):
#         self.var1="var1 is overWritten in class B\n"
#         self.classvar_a="now instance variable is overwritten IN CLASS B\n"
#         super().__init__()
# a=A()
# b=B()
#
# print(b.special,',',b.var1,',',b.classvar_a)

"""in output we can see that output is different from above program.
here b.var1 and b.classvar_a are of class A's intance not B
THIS HAPPENS BECAUSE at first we run var1 and classvar_a
then __init__() of super() will be called now control will move to 
class A's and then constructor of class B will be replaced with 
constructor of class A. so constructor of class A is useless,
you can also remove instance variable of class B's constructor"""









"""      diamond shape problem in multiple inheriance        """





"""this is a problem which creates problem because of multiple inheitance.
programmes get confused on which class uses which method.actually this 
is not a problem in python,but other programming languages like c,c++,
java etc face problem in multiple inheritance.even some programming 
languages don't support it. EXAMPLE - """

# class A:
#     def met(self):
#         print("this is a method in class A")
#
# class B(A):
#     def met(self):
#         print("this is a method in class B")
#
# class C(B):
#     def met(self):
#         print("this is a method in class C")
# class D(C):
#     def met(self):
#         print("this is a method in class D")
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# d.met()
# c.met()
"""this is clear in python that which class is using which method.
but in c or c++ this is a big problem.so programmers avoid
use of multiple inheritance and try to keep program as simple as
possible"""











"""special/dunder methods and operator oveloading"""





# class employee:
#     no_of_leaves = 8
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def print_deails(self):
#         return f"name is {self.name},salary is {self.salary}," \
#                f"role is {self.role}"
#
# emp1 = employee("harry",495,"programmer")
# print(emp1.name)

""" '__init__' this is a special/dunder method.anything start with
double brasses and end with double brasses is called as a dunder or 
special method,eg - '__init__' .we call it dunder init.this is a special
method because it is a constructor.whenever we will make a object like
emp1 we dont have make seperate instance for name,salary&role.we just 
give these details to employee() and constructor __init__ will make them
automatically."""




"""operator overloading"""

"""now if we will make one more object named emp2 and give name,
salary,role to it ,then add emp1 and emp2.error will
come bcz python print() will be confused what to add/join
whether name or salary or role.
to avoid confusion we will take help of dunder add method
like __add__(self,other): """

# class employee:
#     no_of_leaves = 8
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def print_deails(self):
#         return f"name is {self.name},salary is {self.salary}," \
#                f"role is {self.role}"
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
# emp1 = employee("harry",495,"programmer")
# emp2 = employee("rohan",5,"programmer")
# print(emp1+emp2)

"""this is called as operator oveloading.through this we added
2 objects"""






"""there is also a __truediv__()"""

# class employee:
#     no_of_leaves = 8
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def print_deails(self):
#         return f"name is {self.name},salary is {self.salary}," \
#                f"role is {self.role}"
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
#     def __truediv__(self, other):
#         return self.salary / other.salary
#
# emp1 = employee("harry",495,"programmer")
# emp2 = employee("rohan",5,"programmer")
# print(emp1+emp2)
# print(emp1/emp2)


"""use of __reptr__ and __str__"""




"""both these are built-in methods are used to return a 
presentable description about any object rather than default one"""


# class employee:
#     no_of_leaves = 8
#     def __init__(self,aname,asalary,arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def print_deails(self):
#         return f"name is {self.name},salary is {self.salary}," \
#                f"role is {self.role}"
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
#     def __truediv__(self, other):
#         return self.salary / other.salary
#
#     def __repr__(self):
#         return self.print_deails()
#
#     def __str__(self):
#         return f"details are({self.name}{self.salary},{self.role})"
#
# emp1 = employee("harry",495,"programmer")
# print(emp1)
#
# print(repr(emp1))


"""as you can see that both are same.but __repr__ is written by developer
an __str__ is written by end user.it is overwritten to return
a printable string representation of anu user-defined class.
an interesting thing to note here is that priority of
__str__ IS more than __repr__.that means if there would be
both str and repr then str will be executed . 
to execute repr we have to call it exclusively with the object
name in print() like this - 'print(repr(emp1))'."""

"""there are 'more mapping operators to function ',search it in web."""














"""ABSTRACT BASE CLASS AND @abstractmethod"""













"""sometimes we want to make a such class that act like a
bass class.

suppose we have made a rectangle class that print area of rectangle."""
# class rectangle:
#     type = "RECTANGLE"
#     sides = 4
#
#     def __init__(self):
#         self.length = 6
#         self.breath = 5
#
#     def print_area(self):
#         return self.length * self.breath
#
# rect = rectangle()
# print("area is ",rect.print_area())


"""suppose now i want to make a square function that print area square.
now we thought that why not we make a base class named size shape,
that will impose rule to all classes that will inherit shape class.
in this program our rule would be to make a print_area function.
nobody should be able to run class without print_details()"""



# from abc import ABC,abstractmethod
#
# class shape(ABC):
#
#     @abstractmethod
#     def print_details(self):
#         return 0
#
#
# class rectangle(shape):
#     type = "RECTANGLE"
#     sides = 4
#
#     def __init__(self):
#         self.length = 6
#         self.breath = 5
#
#     def print_area(self):
#         return self.length * self.breath
#
# rect = rectangle()
# print(rect.print_area())

"""now if i will try to run rectangle class without
print_details(self): ,ERROR will come. because
base class named shape has ordered to class that has inherit it
to make a print_details() , otherwise i will not allow you to run.
it forces the classes to define print_area()"""












"""    GETTERS , SETTERS AND PROPERTY DECORATOR     """




# class employee:
#
#     def __init__(self,fname,lname):
#         self.fname =fname
#         self.lname =lname
#
#     def email(self):
#         return f"{self.fname}{self.lname}@gmail.com"
#
# ob = employee("romeo","swan")
# print(ob.email())
#
"""now suppose we want to change fname to juliet.then,"""

# ob.fname="juliet"
# print(ob.email)

"""as we can see that the name did not change to.it happens
because at the time of object creation we gave fname as romeo
and at that time constructor runnned not when we gave fname
as romeo"""

"""now email will be changed"""
# ob.fnama = "juliet"
# print(ob.email())
"""but if we want to want to run without running email as a function.
because ENCAPSULATION means to hide the implementation of any 
object or class.so that programmer should not worry about the things inside code
so if you want to give juliet as an attribute so that we can access
email directly without calling email().

for this we take the help of property decorator i.e;@property"""


# class employee:
#
#     def __init__(self,fname,lname):
#         self.fname =fname
#         self.lname =lname
#
#     @property
#     def email(self):
#         return f"{self.fname}{self.lname}@gmail.com"
#
# ob = employee("romeo","swan")
#
# ob.fname = "juliet"
# print(ob.email)
"""so here in above we didn't run email as a function.but now if we
run email as function error will come 
like this - print(ob.email())"""




"""now if we want to give input to email and accoding to that
first name(fname) and last name (lname) will be set.
so for this we have to make a such function that change 
fname and lname accoding to inputed name.
to do this we need to help of 'setter' """


# class employee:
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     @property
#     def email(self):
#         return f"{self.fname}{self.lname}@gmail.com"
#
#     @email.setter
#     def email(self,string):
#         name = string.split("@")[0]
#         self.fname = name.split(" ")[0]
#         self.lname = name.split(" ")[1]
#
#
# ob = employee("romeo","swan")
#
# ob.fname = "juliet"
# print(ob.email)
#
# ob.email = "demon king @gmail.com"
# print(ob.email)

# print(ob.lname)
# print(ob.fname)

"""so in above at first we split
the name at @ sign.so fname &lname is stored in
index 0 and gmail.com is stored in index 1

after that we we split fname and lname.
we stored fname in index 0 and lname in index 1

after if we again chane email then"""

# ob.email = "jack sparrow@gmail.com"
# print(ob.email)
"""now our new email is jacksparrow@gmail.com
we can do this multiple times."""




"""now if we want to delete email named attribute then
in OOP we don't erase we write none.to avoid none we
can give a if else statement that will print email
is not available"""




# class employee:
#
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     @property
#     def email(self):
#         print("setting in......")
#         if self.fname == None or self.lname==None:
#             return f"email is not available/set.plz set again"
#
#         return f"{self.fname}{self.lname}@gmail.com"
#
#     @email.setter
#     def email(self,string):
#         name = string.split("@")[0]
#         self.fname = name.split(" ")[0]
#         self.lname = name.split(" ")[1]
#
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
#
#
# ob = employee("romeo","swan")
#
# ob.fname = "juliet"
# print(ob.email)
#
# ob.email = "demon king @gmail.com"
# print(ob.email)
#
#
#
# del ob.email#email is deleted
#
# print(ob.email)
#
# ##"""we can write a new email after this"""
# ob.email = "romeo juliet@rediffmail.com"
# print(ob.email)
#








"""object introspecton in python"""



"""object introspection means taking out details of an object."""

# class film:
#
#     list = ["rohan","harry","boy"]
#     dict = {"gravity":"apple","boy":"male"}
#
#     def __init__(self,name,profession):
#         self.special = "pirates of caribbean"
#         self.name = name
#         self.profession = profession
#
#     def print_details(self):
#         return f"he is {self.special},his name is {self.name}," \
#                f"his profession is {self.profession}"
#
#
# ob = film("jack sparrow","pirate")


# """now to know about the object ob we do object introspection.
# there ae various ways to do that."""
#
# """type() . it tells the object is of which type"""
# print(type(ob))
# print("this is a string")
#
# """id() .it tells the id of object"""
# print(id(ob))
#
#
# print(id("this is string"))
# print(id("this is string"))
# """you can see that both string has same id"""
#
#
# print(id("this is string"))
# print(id("this .that"))
# "you can see that now they have different id"
#
#
# """dir()"""
#
# print(dir(ob))
# """dir() shows all the methods,attribute,variable which are given.
# it also show those things which can be done"""
#
# o = "dir() stands for directory"
# print(dir(o))
#
#
# """inspect module"""
#
# import inspect
# print(inspect.getmembers(ob))
#
# """it shows all attribute present in 'ob'"""
#





"""there are a lot things on object introspection,search it in internet"""












"""generators in python"""








"""
   iterable,iterator and iteration
--------------------------------------

iterable - iterable is such a python object in which either
           __iter__() or __getitem__() function is defined.
           if we run these 2 function on any object it will
           provide iterator.  

iterator - iterator is such python object in which __next__()
           function is defined.
           
iteration - process of iterating is called as iteration


EXAMPLE - suppose i want to transverse any python object such as list
or a string.let the string is "harry" and we want to access "harry" in
for loop.can we do that or not ? or it tells us wether that object is
iterable or not.if we can iterate that object it means that object is
iterable.if not then object is not iterable

if iterable how can we will iterate?
ans - by running __iter__() or __getitem__() or generating iteration and
if in that iteration,if we will run __next__() repetedly ,then it will
provide next item depending upon how many times we run __next__() function.  
"""



"""generator-
these are iterator(__next__()) which can be used only once.
EXAMPLE - 
"""
# for i in range(78):
#     print(i)

"""the value that range() generate is generatedon 'on fly' means
first 1 is generated then 2 then 3 to 78. it is not that range() first
generated all 78 numbers then print."""


"""suppose we will generate a very big number"""
# for e in range(780000000000000000000):
#     print(e)
"""As you can see in output that it take time to generate number.
this is the proof that range() generate number 'on the fly' . 


WHY WE USE GENERATOR ?
we use generators to Save our RAM. we don't want that a very big number
like 1 trillion or billion would store in memory and slow down our system. 
so we mae a generator that is capable of generating numbers one after another
not at a time.
"""







"""HOW TO MAKE GENERATOR"""


# def generator(n):
#     for h in range(n):
#         yield h
#
#
# g = generator(5)
# print(g)

""" 
'yield' generate numbers 'on the fly'.that means it is a generator.
yield,return and print are different.


in output as you can see that 'g' is the generator,so print()
returned object. 
yield is not a function it's an generator.that is why print() print
a generator object and generator object is generated on fly.
"""




"""now if we don't want generator nor i want to store in RAM
so we just only make a generator and when we will need generator 
we will ue it."""

# def gen(n):
#     for i in range(n):
#         yield i
#
# g = gen(5)
"""so we have made a generator but we don't want numbers
of generator now,so we have just made it. 

to use it we need __next__()"""
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

"""if we will use __next __() once 0 will be printed
if we will use once more 1 will be printed.





to print from 0 to 4 will have to run __next__() 4 times.
instead of doing repetedly we can take help of for loop."""

# def gen(n):
#     for i in range(n):
#         yield i
#
# g = gen(5)
#
# for s in g:
#     print(s)


"""iterable"""


# s = "Despacito"
# for c in s:
#     print(c,end=" ")

"""if we print c we get output as 'D e s p a c i t o' because string is iterable.
 because a iterator is already defined by python with string by default"""


"""you can also use next function with a string."""
# f = "whosays?"
# ier=iter(f)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())













"""list comprehension in python"""










"""comprehension is of 4 types - list comprehenon,ditionary comprehenion,
set comprehension and generator comprehension

comprehension in simple words is a way to reduce code.
EXAMPLE - 
suppose you want to print all even numbers between 100 in list then
we will do like below
"""
# list = []
# for item in range(101):
#     if item%2==0:
#         list.append(item)
# print(list)


"""as you can we did it.but we can do this in just one line with
the help of comprehension"""


# list=[item for item in range(101) if item%2==0]
# print(list)
# print(type(list))

"""so first we gave item as variable to store numbers coming from if statement.
then for loop give the numbers divisible by 2 with the help of if statement
and store it in item."""











"""dictionary comprehension"""












"""suppose you want to make a dictionary to print like this
{0:"item0",1:"item1",2:"item2"......,100:"item100"

there are to ways one is to write them individually but it is time consuming
other is to take the help of comprehension
"""

# dict = {i: f"item{i}" for i in range(101)}
# print(dict)


"""now if we want to swap key and value of dictionary."""

# dict = {i: f"item{i}" for i in range(101)}
# dict1 = {value:key for key,value in dict.items()}
# print(dict1)
#
# print(dict)
"""As you an see that key and value of dict have exchanged their data.
in dictionary by default key comes first than value comes.but we made the value
to come 1st them key."""











"""Set comprehension"""











"""this is also like list and dictionary comprehension.the only difference is we can
take value only one time."""

# dress = {dress for dress in ["dress0","dress2", "dress0","dress2"]}
# print(dress)
#
# print(type(dress))

"""as you can we get output but dress0 and dress2 print
same things only one time,but from last.so it print dress2 first then dress0.
if dress0 would be in last and before that dress0 would be present. then
output would be {'dress0', 'dress2'}"""










"""generator comprehension in python"""






"""to make generator we have to use paranthesis i.e;() """

# even = (i for i in range(5) if i%2==1)
# print(even)
#
# print(even.__next__())
# print(even.__next__())
# print(even.__next__())

"or instead of using __next__()repetedly,use for loop."

# even = (i for i in range(100) )
# print(even)
#
# for x in even:
#     print(even.__next__())







""" using else with for loop or 'for else' """

# list = ["demon","king","finn","barlor"]

# for x in list:
#     print(x)
#
# else: print("else statement succesfully runned.")

"""in above you can see that we used else statement after for loop.
but ele statement will only run only if for loop don't have any break statement.
like below"""
# for z in list:
#     print(z)
#     break
#
# else: print("else statement succesfully runned.")


"""usage of 'for else' """


"""suppose you have a list and you want to print an element
from list which is not present like vampire,then else statement will
be executed"""
# list = ["demon","king","finn","barlor"]
#
# for y in list:
#     if y == "vampire":
#         break
#
# else : print("else statement successfully executed")




'''but if you print any element from list which is present,then else
statement will not be executed'''

# list = ["demon","king","finn","barlor"]
# for y in list:
#     if y == "king":
#         print(y)
#         break
# else : print("else statement successfully executed")








""""FUNCTION CACHING IN PYTHON"""






"""SUPPOSE WE DO SOME WORK and it take some time like 3 second
here we will assume that time.sleep() is that work which take 3 second to do some work"""

# import time
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     print("work done")

"""as you can see in output that after printing 1st print statement execution stop for 3 second
and then it print 2nd print statement."""


"""now suppose we have to use some_work(3) which take 3 second,10 times.then we have to use it manually,
but that is time taking.so instead of that we can store that 3ec in a variable, and use the variable instead
of using sleep() again and again. now if we want that python should do all those stuffs not we,that is called
as function caching"""

"""so when we do that a cache is created.this thing is used mostly when we use internet.
suppose we are accessed a you-tube page for the 1st time,so our computer will go to browser,then go to net,
then search for you tube page. and then save it somewhere in our local disk by default,so that when we will
access that same page through any browser,our computer will give/load from local disk not from internet.it 
save time and it increase the speed.it will show that page unless the computer know that page is updated."""

"""for this example, we can store the value of some_work() i.e;3 somewhere like in a variable or
somewhere else (this will be done by python automatically) so that when we will use it again python,
python will give that value 3 from that stored location."""









# import time
# def some_work(n):
#     time.sleep(n)
#     return
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     print("work done")
#     some_work(3)
#     print("work is done again")

"""in above code 1st print statement will be printed then execution stop for 3 sec,then 2nd print statement
will be printed then again execution stop for 3sec then 3rd print statement will be printed.
but if we want that after printing 2nd print statement,3rd print statement should be printed immediately
i.e; second time.sleep() will not be executed.
for that we will take the help of lru_cache.it is a decorator"""


# import time
# from functools import lru_cache
#
# @lru_cache (maxsize=3)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     print("work done")
#     some_work(3)
#     print("work is done again")

"""so you can see in output that 2nd some_work(3) did not execute.

so we imported lru_cache from functools.it is a type of decorator.
we used maxsize=1,so it ask how many value you want to cache,we gave 3.
that it will cache latest 3 value.

now the value 3 of some_work() is stored/cached by lru_cache.
in simple words if we will use some_work(3) multiple times only one time it will be executed.
like below---"""


# import time
# from functools import lru_cache
# @lru_cache (maxsize=3)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     print("work done")
#
#     some_work(3)
#     print("work is done again")
#     some_work(3)
#     print("work is done again")
#     some_work(3)
#     print("work is done again")
#     some_work(3)
#     print("work is done again")
#     some_work(3)
#     print("work is done again")

"""
but remember if we will pass the value as 2 or anything else then 2 sec will be delayed.
because we cached the value 3 of some_work() not any other number.

as we discussed above that when we access a you-tube page for the 1st time,our computer will go to browser,then go to net,
then search for you tube page. and then save it somewhere in our local disk by default,so that when we will
access that same page through any browser,our computer will give/load from local disk not from internet.

above also same thing happened value 3 is saved somewhere and when we will use the value 3 multiple times,python
will give 3 from saved location ,it will not generate again.so that's when we use some_work(3) 6 times
only 1 time it is executed.after printing 2nd print statement other 4 print statement were executed immediately,
because python gave it from saved location,it did not generate 5 times.if it has geneated 5 times then total 18sec
will be taken to finish execution.but it has taken only 3second.so it saved time and increased speed.
"""
# import time
# from functools import lru_cache
# @lru_cache (maxsize=3)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     print("work done")
#
#     some_work(5)
#     print("work is done again")

"""here when we gave 5.
execution 1st stop for 3 sec and then for 5 sec.
it happens because 3 is cached by python not 5."""




# import time
# from functools import lru_cache
# @lru_cache (maxsize=3)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     some_work(2)
#     some_work(5)
#     some_work(4)
#     print("work done")
#
#     some_work(3)
#     print("work is done again")

"""now 2,5 and 4 is cached not 3.so after printing 'work done', execution stop for 3sec.


we gave max value as 3 means python can cache 3 different value,but in main
main function we gave 4 different value to cache.

so python will first cache 3,2 and 5 . Then,when it will see that one more value is present to
cache so instead of 3 it will cache 4. now cached value are 2,5 and 4. 

"""

# import time
# from functools import lru_cache
# @lru_cache (maxsize=3)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     some_work(2)
#     some_work(5)
#     some_work(4)
#     print("work done")
#
#     some_work(2)
#     some_work(5)
#     some_work(4)
#     print("work is done again")
"""as you can see after printing 'work done' 2nd print statement is printed immediately,
because 2,5 an 4 are cached/stored.

but if we will increase maxsize to 45 then 3 will also be cached
"""
# import time
# from functools import lru_cache
# @lru_cache (maxsize=45)
# def some_work(n):
#     time.sleep(n)
#     return n
#
# if __name__ == '__main__':
#     print("now running some work")
#     some_work(3)
#     some_work(2)
#     some_work(5)
#     some_work(4)
#     print("work done")
#
#     some_work(3)
#     some_work(2)
#     some_work(5)
#     some_work(4)
#     print("work is done again")

"""here main function is not necessary.you can also do these without main function."""











"""try, except, else and finally"""



# try: open("harry.txt")
#
# except Exception as e: print(e)
#
# else : print("it will run if except don't run")
#
# finally : print("it will run at any cost")


"""else statement run if except don't run.in more simple way
as try it run a threw a error.and that error goes to except,and error is printed.that means
else statement runned.


EXAMPLE OF ELSE STATEMENT WILL RUN - """

# try: print("now else will run because except will not run .")
#
# except Exception as e: print(e)
#
# else : print("it will run if except don't run")
#
# finally : print("it will run at any cost")





"""COROUTINES IN PYTHON"""




'''SOMETIMES when we run or use a function that is time consuming such as task related
to machine learning or deep learning or a file containing lakhs of file..
in such cases we want that at first when we run a function,execution will be half
when we run for 2nd time it will run from the half part not from top again
so for that we use coroutine to make program more efficient and fast.
'''

# import time
# def searcher():
#     file = "this file belongs to demon king" \
#            " and you cant use it, it's dangerous"
#     time.sleep(3)

"""now assume that 'file' is a very big file and it take 30 minute to
be read by computer (we have used time.sleep to stop execution for 3 sec.
assume execution stop for 30 second completly).

now searcher() is not a coroutine.to make it act like a coroutine we 
need to use an infinite loop and yield statement

EXAMPLE - 
"""
# import time
# def searcher2():
#     file = "this file belongs to demon king" \
#            " and you cant use it, it's dangerous"
#     time.sleep(3)
#
#     while True:
#         text = (yield)
#         if text in file:
#             print("present in the book")
#         else: print("not present")
#
# search = searcher2()
# next(search)
# search.send("demon")
#
# input("press any key")
# search.send("belongs to")
# input("press any key")
# search.send("it's dangerous")

"""so yield generate numbers one the fly or at the time of execution.
so when we'll store yield in text searcher() will act as a coroutine.

next is used to start the coroutine

'send' is used to send the value to searcher()

PROCESS - now when we'll send something to searcher() at first execution will start from top
and wait for 3 second and then i will enter to while loop to check
whether the letter 'demon' is present or not.

but from the next values i.e;input() we dont have to wait for 3 second again
,because execution will be skipped to while loop.
in simple words we send the letter 'belongs to' searcher() but searcher()
will skip time.sleep() and give word to 'yield' and then condition will be chequed.

so searcher act like a coroutine and saved our time 
. 

 """








""" os module in python + examples"""

"""os module is a built in module in python. os stands for operating system.
in our pc we have also operating system like windows,linux,etc... . It controls
all hardware of computer like mouse,keyboard,monitor . it makes them play like 
a team."""

#import os

# print(dir(os))#dir = directory
# '''['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREATE',....]
# as you can see these are all those things which we can do with os module.'''


# print(os.getcwd())#cwd = current working directory
# '''it shows the current location,where files are stored.
# when we don't give the exact location of file ,python search that file in
# current location or current directory'''



# os.chdir("E:/") #change directory
# """it is used to change location of current directory.
# to verify use getcwd()"""
# print(os.getcwd())



# print(os.listdir())
# """it showed the list of all files stored in current location i.e;c://(in my pc).
# to see the list of all files present in disk E:// write :"""
# print(os.listdir("E:/"))


#print(os.mkdir("lauv"))#create a new folder in curent location



# print(os.makedirs("this/that"))
# '''create 2 folder named this and that.that folder will be inside this folder.'''

# os.rename("food","ood")
# '''change the name food name to ood.'''



# print(os.path.exists("c://"))
# '''it tells whether path exist or not.if path exist
# output will be True otherwise False.'''
# print(os.path.exists("c:/garry"))







"""requests module in python"""

"""request module is not inbuilt in python,so you have to downloads it.
and also you need internet connection"""


#import requests

# r = requests.get("https://www.facebook.com/")
# print(r.text)


# url = "https://www.facebook.com/"
# data = {'name':'xxxxxxx','password':'xxxxxxxxxxx'}
# r = requests.post(url=url,data=data)
# print(r.text)
#
# print(r.status_code)








"""json module in python"""




"""json is an inbuilt module in python.
json stands for java script orientation quotation.it is a data inter-change format,
derived from javascript. it is mostly use for storing and transferring data.
so if we want our program to interact with internet,we must familiar with
json module,even only to send or receive data through internet.
however ,if we want our program to interact only a bit through internet,
we must import json module first.
format to write a json is ( '{ }' ) """

# import json


'''
use of json.loads  - 
convert json to dictionary'''
# data = '{"var1":"56","var2":"65"}'
#
# parse_json = json.loads(data)#convert json into dict
# print(parse_json)
# print(type(data))

"""parse_json means convert string into json and you 
can use that string in javascript
json.loads convert json into dictionary"""




"""
use of json.dumps()  - 
convert dict to json/jvascript"""
# data2 = {"channel name":"codehack","cars":('bmw',"audi"
#         ,"tesla")}
#
# convert = json.dumps(data2)
# print(convert)

"""

"""
# data3 = {"channel name":"codehack","cars":('bmw',"audi"
#         ,"tesla"),"isbad":False}
#
# convert = json.dumps(data3)
# print(convert)
# print(type(data3))

"""
json.dumps() convert data2(dict) into javascript.
To know that open any browser but i will use google chrome,
and then right click on your mouse and go to inspect .
a dialog box will appear and then click on console tab.

copy your output in pycharm and then paste on console tab 
and then press enter you will get output.

but if you copy and paste the variable 'data3' 
you will get an error.
because in python 'False' start with a capital letter
but in java 'false' start with small letter
you can see the difference in output.

explore more about console tab and json in internet
"""









"""pikle module in python and its uses"""








'''pickle is a inbuilt module in python.actually pickle
is a dish we used to eat.in hindi it is called as "achar".
we can store or preserve it for a long time and use it
whenever we want to eat.

Samewise in python pickle is an inbuilt module.we use pickle to store
data in file directly without creating a file,pickle will create
and store automatically.And we can use that whenever we want.
and this process is called pickling'''


# import pickle

# cars = ["audi","maruti suzuki","hero","BMW"]
# file = "mycar.pkl"
#
# """in python each and everyting is stored in form of object."""
# fileobj = open(file,"wb")#open it in binary mode
#
# pickle.dump(cars,fileobj)
# '''pickle.dump takes 2 argument,an object
# and a file object'''
#
# fileobj.close()
#
"""when you run the above code a file will be created
automatically.you cannot acccess it directly,you have
to access it through pickle only."""





'''NOW HOW ACCESS THE PICKLED/STORED DATA.'''




'''car list is stored in form of object'''
# file = "mycar.pkl"
# fileobj = open(file,"rb")#binary mode is compulsory
# mycar = pickle.load(fileobj)
# print(mycar)
# print(type(mycar))




"""          raising exceptions in python            """


'''There is a built-in 'raise' keyword in python.'''

# a = input("enter your name : ")
#
# if a.isnumeric():
#     pass

###some hundred codes and it takes 1 hour to run

'''suppose we have have some hundred codes below if statement.
now we want that, if a's input is wrong the program should stop
at if statement and our time would be saved.
so to da that we will raise an exception error if input of a is
wrong'''

# a = input("enter your name : ")
#
# if a.isnumeric():
#     raise Exception("int variables are not allowed")

###some hundred lines of code that take 1hour

'''in output if you type 5 then a error will come
and out message will be displayed i.e;int variables are not allowed.
but in output if you type 'harry' then no error will come'''


"""zero division error"""
# a = input("enter your name : ")
# b = input("enter your salary : ")
#
# if int(b)== 0 :
#     raise ZeroDivisionError("b is 0 so stopping execution")
# elif a.isnumeric():
#     raise Exception("int variable is not allowed")
###some hundred lines of code that take 1hour
"""if in output if we input b as 0 then error will come,
but if we input b as 56 or something else then output will not come"""

"you can also do like this"
# c = input("enter your age : ")
# if int(c)<18:
#     raise ZeroDivisionError("b is 0 so stopping execution")



"""use of value error with try except"""
# c = input("enter your name : ")
# try :
#     print(a)
# except Exception as e :
#     if c == "harry" :
#         raise ValueError("employee harry is not allowed")

"""in output if we type harry we will get 2 error.
the 1st error will be printing wrong variable
and 2nd error will be of value error"""




"""there are a lot of built-in error in python 
which you can rise. EXPLORE THOSE IN INTERNET"""





"""DIFERENCE BETWEEN 'is' and '==' in python."""

"""

==  - value equality
    - two objects have same value

is  - reference error
    - two reference refer to same objects(objects may be diferent)


suppose we have 2 objects car and bike
now car's value is 5 and bike's value is also 5

car == bike   True
because value of car and bike is same even though
car and bike are different objects

car is bike   False
because car and bike are 2 different objects

so == compare value of 2 different/same objects
'is' compare 2 objects whether they are sam or not
"""



"""          creating a command line utility              """


"""a command line utility is a way of giving operating system instruction
using lines of text.command line program operate through command line
or window powershell."""

# import argparse
# import sys
#
# def calc(args):
#     if args.o == 'add':
#         return args.x + args.y
#
#     elif args.o == 'sub':
#         return args.x - args.y
#
#     elif args.o == 'mul':
#         return args.x * args.y
#
#     elif args.o == 'div':
#         return args.x / args.y
#
#     else : return "something went wrong"
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()#this is an object from argument parser class
#
#     parser.add_argument('--x',type=float,default=1,help="enter first number")
#     parser.add_argument('--y',type=float,default=1,help="enter second number")
#     parser.add_argument('--o',type=str,default='add',help="tell what you want to do")
#
#     args = parser.parse_args()
#     sys.stdout.write(str(calc(args)))

