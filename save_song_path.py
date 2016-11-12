#! /usr/bin/env python
import os,time

song = ''

def get_song_path():
    pid = 0
    try:
        pid = int(os.popen('pgrep -x vlc').read())
    except ValueError:
        return ''
    process = "readlink /proc/" + str(pid) + "/fd/*"
    files = os.popen(process).read()
    for item in files.split("\n"):
        if "/run/" in item:
            song_path = item.strip() + '\n'
            return song_path



def save_song_path():
     pid = int(os.popen('pgrep -x vlc').read())
     process = "readlink /proc/" + str(pid) + "/fd/*"
     files = os.popen(process).read()
     for item in files.split("\n"):
         if "/run/" in item:
             global song
             song = song_path = item.strip() + "\n"
             txt = open(".songslist.txt", "r")
             if song_path in txt.read(): # if the song path present in file, increase its frequency by 1
                txt.seek(0)
                data = txt.readlines()
                txt.close()
                i = 0
                prevline = None
                for line in data:
                    if song_path == line:
                        freq = int(prevline)
                        freq = freq + 1
                        data[i-1] = str(freq) + "\n"
                        f = open(".songslist.txt","w")
                        f.write(''.join(data))
                        f.close()
                    i = i + 1
                    prevline = line.strip("\n")



             else:                 # appending the song path to the list
                 txt = open(".songslist.txt", "a")
                 txt.write("1")
                 txt.write("\n")
                 txt.write(song_path)
                 txt.close()


def main():
    processname = 'vlc'
    global song
    while 1:
        song = ''
        time.sleep(1)
        tmp = os.popen("ps -Af").read()
        proccount = tmp.count(processname)
        while proccount > 0:
            tmp_song = get_song_path()
            if tmp_song != song:
                save_song_path()
            time.sleep(1)
            tmp = os.popen("ps -Af").read()
            proccount = tmp.count(processname)




if __name__ == "__main__":
    main()
