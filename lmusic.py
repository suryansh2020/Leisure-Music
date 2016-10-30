import os
import time

# We will read a song and save its frequency using save_song function
def save_song():
    txt = open(".songslist.txt", "r+")
    pid_file = open(".pid.txt", "r+")
    tmp = int(pid_file.read())
    pid = 0
    try:
        pid = int(os.popen('pgrep -x vlc').read())
    except ValueError:
        return
    if pid == tmp:
        return
    pid_file.seek(0,0)
    pid_file.write(str(pid))
    process = "readlink /proc/" + str(pid) + "/fd/*"
    files = os.popen(process).read()
    for item in files.split("\n"):
         if "/media/" in item:
             text = item.strip() + '\n'
             if text in txt.read(): # if the song path present in file, increase its frequency by 1
                 txt.seek(-2,1)
                 freq = int(txt.read())
                 freq = freq + 1
                 txt.seek(-2,1)
                 txt.write(str(freq))
                 txt.close()

             else:                 # appending the song path to the list
                 txt = open(".songslist.txt", "a")
                 txt.write(text)
                 txt.write("1")
                 txt.write("\n")
                 txt.close()




# play_song() function will calculate average frequency of songs and will play the song having above average frequency
def play_song():
    txt = open(".songslist.txt", "r")
    lines = txt.read().splitlines()
    sum = 0
    ctr = 0
    for line in lines:
        if line.isdigit():
            sum = sum + int(line)
            ctr = ctr + 1
    average = sum/ctr
    ct = 0
    for line in lines:
        if line.isdigit():
            if int(line) >= average:
                ct = 1
                continue
        if ct == 1:
            song = "vlc " + '"' + line + '"'
            os.popen(song)
            break


def main():
    while 1:
        save_song()
        idle_time = int(os.popen("xprintidle").read())
        if idle_time > 10000:
            play_song()

if __name__ == "__main__":
    main()
