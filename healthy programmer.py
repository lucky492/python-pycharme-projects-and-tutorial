"""
HEALTHY PROGRAMMER


assume that a person work at office from 9 to 5pm.
we have to take care of his health by reminding 3 things
1st - to drink water after every 40 minute
2nd - to do eye exercise after every 30 minute
3rd - to perform some physical exercise after every 60 minute

the task is to create a program that remind him by playing mp3 song
until user type drunk for water,'eyedone' for eye exercise and
'exdone' for physical exercise.

after user enter the input the music should stop and
a file would create ,which will
contain details about date and time and task performed


challenge - you will have to take care that reminder
            should not play at same time
          - use pygame module to play audio
# """

from pygame import mixer
from datetime import datetime
from time import time

def musicplay(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
         if stopper == input("enter stopper : "):
             mixer.music.stop()
             break

def store_details(msg):
    with open("healthy programmer details.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    watertime = time()
    eye_ex = time()
    exercise = time()


    while True:
        if time()- watertime > 60*30:
                    musicplay("Serhat Durmus - Hislerim (Bass Boosted).mp3","d")
                    watertime = time()#reinitialize time
                    store_details("drunk water at :")

        if time()- eye_ex > 60*35:
                    musicplay("Serhat Durmus - Hislerim (Bass Boosted).mp3","d")
                    eye_ex = time()
                    store_details("eye exercise at :")

        if time()- exercise > 60*40:
                    musicplay("Serhat Durmus - Hislerim (Bass Boosted).mp3","d")
                    exercise = time()
                    store_details("exercised at at :")
                    break

    print("thank u for using")
