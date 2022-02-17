"""create a health management system
you have 3 client named harry, rohan ,mohammad,
you have to manage these three and give them what to eat and exercise
and also record what they ate and exercised including time inside square bracket []
create 3 files for food and 3 for exercise.total 6 files
write a function that when executed takes input as client name.
and ask to press 1 to record time and 2 to record exercise

use this below function to record time
def getdate():
    import datetime
    return datetime.datetime.now()
"""
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c = int(input("enter 1 for food and 2 for exercise"))
        if c==1:
            value = input("enter what you ate : ")
            with open("harryfood.txt","a") as f:
                f.write(str([str(gettime())]) + ":" + value )
            print("successfully recorded")

        elif c==2:
            value = input("enter what workout you did today : ")
            with open("harryex.txt","a") as f:
                f.write(str([str(gettime())])+ value )
            print("sucessfully recorded")

        else:
            print("invalid entry")

    else:
        print("enter 1 for harry,not othes numbers")

def retrive(k):
    if k==1:
        v = int(input("enter 1 for food and 2 for exercise"))

        if (v==1):
            with open("harryfood.txt") as op:
                for i in op:
                    print(i,end=" ")

        elif v==2:
            with open("harryex.txt") as op:
                for i in op:
                    print(i, end=" ")

    else:
        print("enter valid number")

print("health management system")

a=int(input("press 1 to record and 2 to retrive or show "))

if a==1:
    b=int(input("press 1 for harry "))
    take(b)

else:
    b=int(input("press 1 for harry "))
    retrive(b)

