import os
import subprocess
import youtube_search

if(os.stat("playlist.txt").st_size)>0) {
	with open('playlist.txt', 'r') as playlist
    	song_name = playlist.readline().strip()

    url = youtube_search.search(song_name)
	cmd = "youtube-dl -f 140 -o - " + url + 
		"| vlc-wrapper --novideo --intf dummy -; if [ $(cat autoplay.txt) -eq "1" ]; then deque.py; play.py; fi;"
	subprocess.Popen(cmd)


}