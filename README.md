# Leisure-Music
A python script to play your favorite song when you are idle on your Fedora/Linux system

# How does it works?

This project consists of two scripts viz. save_song_path.py and play_song.py

1. Firstly, make the scripts executable by using command ```chmod +x save_song_path.py``` and ```chmod +x play_song.py```

2. Add the scripts to run at startup by writing ```.desktop``` files in ```.config/autostart``` directory

3. Make a file ```.songslist.txt``` into your home directory

### About ```save_song_path.py```

This script identifies the path of song being played in VLC media player only and it saves the song path into the file ```.songslist.txt``` and increases the frequency (number of times the song is being played) by one. 
Thus at the end, we have a file which consist of a list of songs being played by the user and the frequency of the songs being played.

This script runs throughout the session and always writes the song's path and thus increases its frequency.

### About ```play_song.py```

This script calculates the average of the frequency of all the songs being played and playes randomly a song which have the frequency greater than or equal to the average frequency along when the system is idle for 4 minutes. 
