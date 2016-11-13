#! /usr/bin/env python
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

    txt.close()
    a = 0
    b = len(song_list) - 2
    while 1:
        c = randint(a,b)
        if c % 2 == 0:
            if int(song_list[c]) >= average:
                song = 'vlc ' + '"' + song_list[c+1] + '"'
                os.popen(song)
                break


if __name__ == "__main__":
    while 1:
        if int(os.popen('xssstate -i').read()) >= 180000: # idle time for 3 minutes
            play_song()
        time.sleep(60)
