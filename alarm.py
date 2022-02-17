"""
this is a python program that is a reminder
 for eg - you want to drink water after every 1 hour
        it will play song after every hour

and also an alarm clock
"""
def play_song(file,snooze):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    # play music for mentioned time
    t = time()
    while mixer.music.get_busy():
        if time()-t > snooze:
            mixer.music.stop()
            t = time()
            break

def alarm(timer,snooze,msg):
    while True:
        now = datetime.now()
        current_time = now.strftime("%I:%M")

        if current_time == timer:
            print(current_time + "=" + timer)
            notification.notify(title = "Alarm",
                                message = msg)
            mixer.init()
            mixer.music.load("Serhat Durmus - Hislerim (Bass Boosted).mp3")
            mixer.music.play()

            t = time()
            while mixer.music.get_busy():
                if time() - t > snooze:
                    mixer.music.stop()
                    t = time()
                    exit()

if __name__ == '__main__':
    from pygame import mixer
    from time import *
    from plyer import notification
    from datetime import datetime

    a = input("Enter 1 to use reminder and 2 to alarm : ")
    i = 0
    while i<=1:
        if a == "1":
            msg = [ ]
            play_after = [ ]
            x = int(input("Enter no of timers : "))
            for x in range(1,x+1):
                msg.append(input("Enter your message : \n"))
                play_after.append(int(input("Enter the time interval in secs")))
            snooze_time = int(input("Enter snooze time in secs"))
            song = "Serhat Durmus - Hislerim (Bass Boosted).mp3"

            # return no of seconds passed
            #time begin from here
            #this is for reminder
            time_start = time()
            i=0
            while True:
                try:
                    if time()-time_start >= play_after[i]:
                        notification.notify(title="Reminder",
                                            message=msg[0],
                                            timeout=play_after[0]-1)
                        i = i + 1
                        play_song(song,snooze_time)
                        # restart time again
                        time_start = time()
                except Exception : pass

                if time()-time_start >= play_after[0]:
                    notification.notify(title = "Reminder",
                                        message = msg[0],
                                        timeout = play_after[0]-1)
                    i = i + 1
                    play_song(song,snooze_time)
                    # restart time again
                    time_start = time()

        # board = ["","","",""]
        # def hrs_board():
        #     print(board[0] + "_", board[1] + "_")
        #
        # def min_board():
        #     print(board[0] + "_", board[1] + "_")

        if a == "2":
            hour = input("Enter hour(use 0 before hour if required):\n")
            min = input("Enter minute(use 0 before min if required):\n")
            a = hour + ":" + min
            s = int(input("Enter snooze time in sec : "))
            msg = input("Enter your message : ")
            alarm(a, s,msg)
            break
    i = i+1