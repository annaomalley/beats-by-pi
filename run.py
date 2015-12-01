from flask import Flask, request, render_template
import random
import os
import subprocess
import youtube_search

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_action():
    with open('current_song.txt', 'r') as songfile:
        curr_song = songfile.read()
    return render_template('playing.html', song=curr_song)

@app.route('/', methods=['POST'])
def post_action():
    body = request.form.get('Body')
    if body =='#stop'
        change_mode('0')
        os.system('pkill vlc')
    elif body == '#queue'
        change_mode('1')
        os.system('pkill vlc')
        subprocess.Popen('python play.py') 
    else
        if check_mode() == '0'
            url = youtube_search.search(body)
            os.system('pkill vlc')
            cmd = "youtube-dl -f 140 -o - " + url + "| vlc-wrapper --play-and-exit --novideo --intf dummy -"
            subprocess.Popen(cmd, shell=True)
        else
            fo = open('playlist.txt', 'a')
            fo.write(body + '\n')
            fo.close()
    return 0

def change_mode(mode):
    fo = open('autoplay.txt', 'w')
    fo.write(mode)
    fo.close();

def check_mode():
    fo = open('autoplay.txt', 'r')
    mode = fo.read(2)
    fo.close()
    return mode

@app.route('/error', methods=['GET','POST'])
def error_action():
    return render_template('reply_error.xml')

if __name__ == '__main__':
    open('playlist.txt', 'w').close()
    fo = open('autoplay.txt', 'w')
    fo.write('0')
    fo.close()
    app.run(host='0.0.0.0', port=80)
