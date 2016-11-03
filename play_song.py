#! usr/bin/env python
import os,time
from random import randint

def play_song():
    sum = 0
    count = 0
    txt = open(".songslist.txt", "r")
    song_list = txt.read().splitlines()
    for i,val in enumerate(song_list):
        if val.isdigit():
            sum = sum + int(val)
            count = count + 1
    average = sum / count
    #average is calculated




if __name__ == "__main__":
    while 1:
        if int(os.popen('xprintidle').read()) >= 240000: # idle time for 4 minutes
            play_song()
        time.sleep(30)
