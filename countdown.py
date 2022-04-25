import time

def countdown(tyme):
    while tyme:
        mins, secs = divmod(tyme, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        tyme-=1
    print("Time's up")

countdown(60)