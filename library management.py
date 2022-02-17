"""
python OOP mini project
a library management system or a online library manager

you have to make a library class & you have to define some methods


1st - define a method to display all books present in library
2nd - if someone lend book ask his name and store it.for this create a method
3rd - if someone want to donate book in library,make a function to named add book
4th - if you have to return a book,define function that will return book

purpose

suppose if i want to make a class using this library
harry_library = library(list of book name,library name)

you can make a dictionary that will maintain which person took which book
key will be books,value will be name of person

create a main function and run an infinite loop asking user for their input.the input
will be of 4 types.what user want to read/lend/add/return

"""
books = ["six easy pieces", "selina math", "physics",
        "geography", "accounting","twilight","dead poets society",
         "ikigai"]

dict = {"rohan": "geography","harry":"computer",
        "frank":"twilight"}

'''library management system'''

class library:
    def __init__(self,book,librayname):
        self.books= book
        self.libraryname = librayname


    def display_book_list(self):
        print("\t\t\there are your books")
        for i in books:
            print(i)
        print("\t\t\tthank u for visiting")



    def show_dict(self):
        for keys,values in dict.items():
            print(f"{keys} took {values}")



    def lend_book(self):

        if value in books:
            dict.update({key:value})
            print("\t\t\tsuccessfully lended")
            print("\t\t\tthank u for lending book")
            print("new names are : ")
            harry.show_dict()
        else: print(" \t\t\tsorry book is not available")


    def donate_book(self,d):
        books.append(d)
        print("\t\t\tsucessfully added")
        print("\t\t\tnew books are")
        harry.display_book_list()




    def return_book(self):
        rb = input("book which have to be returned : ")
        gh = input("enter your name,if you have borrowed book : ")

        if rb in dict:
            print("yes you can return")

        elif gh in dict:
            del dict[gh]
            print(f"\n{gh} sucessfully returned {rb}\n")
            harry.show_dict()
            print("\n\t\t\tthank u for returning")

        else: print(f"{gh} did not took book \n")


if __name__ == '__main__':

   while True:
       try:
           harry = library("ikgai", "demon's library")

           print("\t\t\twelcome to harry library")

           print("\n\npress 1 to see books\n"
                 "press 2 to donate books\n"
                 "press 3 to see list of persons took books\n"
                 "press 4 to lend book\n"
                 "press 5 to return book\n"
                 "press 7 to exit")
           s = int(input("\nwhat you want to do : "))


           if s == 1 :
             harry.display_book_list()

           elif s == 2 :
               g=input("enter book name : ")
               harry.donate_book(g)

           elif s == 3 :
               harry.show_dict()

           elif s == 4 :
               key = input("plz enter your name : ")
               value = input("enter book name you want to borrow :")
               harry.lend_book()


           elif s == 5:
              harry.return_book()


           elif s == 7:
               print("thank u for visiting")
               break
       except Exception as e : print("\n\t\t\t invalid input plz try again")

