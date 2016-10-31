import os,time

song = ''

def get_song_path():
    txt = open(".songslist.txt", "r+")
    pid = int(os.popen('pgrep -x vlc').read())
    process = "readlink /proc/" + str(pid) + "/fd/*"
    files = os.popen(process).read()
    for item in files.split("\n"):
        if "/media/" in item:
            song_path = item.strip() + '\n'
            return song_path



def save_song_path():
     txt = open(".songslist.txt", "r+")
     pid = int(os.popen('pgrep -x vlc').read())
     process = "readlink /proc/" + str(pid) + "/fd/*"
     files = os.popen(process).read()
     global song
     for item in files.split("\n"):
         if "/media/" in item:
             song = song_path = item.strip() + '\n'
             if song_path in txt.read(): # if the song path present in file, increase its frequency by 1
                 byte = len(song_path)
                 txt.seek(-(byte+2), 1)
                 freq = int(txt.readline())
                 freq = freq + 1
                 txt.seek(-2,1)
                 txt.write(str(freq))
                 txt.close()

             else:                 # appending the song path to the list
                 txt = open(".songslist.txt", "a")
                 txt.write("1")
                 txt.write("\n")
                 txt.write(song_path)
                 txt.close()


def main():
    processname = 'vlc'
    tmp = os.popen("ps -Af").read()
    proccount = tmp.count(processname)
    while proccount > 0:
        tmp_song = get_song_path()
        if tmp_song != song:
            save_song_path()
        time.sleep(30)




if __name__ == "__main__":
    main()
