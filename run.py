#!/usr/bin/python

from flask import Flask, request, render_template
import random
import os
import subprocess
from subprocess import check_output
import youtube_search
import sys
import traceback

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_action():
    with open('current_song.txt', 'r') as songfile:
        curr_song = songfile.read()
    return render_template('playing.html', song=curr_song)

@app.route('/', methods=['POST'])
def post_action():
    try:
        body = request.form.get('Body')
        if body =='#stop':
            print('[RECEIVED] STOP request') 
            change_mode('0')
            os.system('pkill vlc')
            return "Success: STOP"
        elif body == '#queue':
            print('[RECEIVED] QUEUE request')
            change_mode('1')
            os.system('pkill vlc')
            subprocess.Popen('./play.py') 
            return "Success: QUEUE MODE ON"
        elif body == '#next':
            if check_mode() == '1':
                print('[RECEIVED] NEXT request')
                os.system('pkill vlc')
                return "Success: NEXT"
            return "Fail: Not in queue mode"
        else:
            if check_mode() == '0':
                print('[RECEIVED] PLAY request')
                url = youtube_search.search(body)
                if url is None:
                    return "Fail: Could not find song"
                os.system('pkill vlc')
                cmd = "youtube-dl -f 140 -o - " + url + "| vlc-wrapper --play-and-exit --novideo --intf dummy -"
                subprocess.Popen(cmd, shell=True)
                return "Success: PLAYING '" + body + "'"
            else:
                print('[RECEIVED] ADD request')
                fo = open('playlist.txt', 'a')
                fo.write(body + '\n')
                fo.close()
                if not is_process_running('vlc'):
                    subprocess.Popen('./play.py')
                return "Success: ADDED TO QUEUE '" + body + "'"
    except Exception, err:
        print(traceback.format_exc())
    return "Success" 

def change_mode(mode):
    fo = open('autoplay.txt', 'w')
    fo.write(mode)
    fo.close();

def check_mode():
    fo = open('autoplay.txt', 'r')
    mode = fo.read(2)
    fo.close()
    return mode

def is_process_running(name):
    try:
        process_id = get_pid(name)
        os.kill(process_id, 0)
        return True
    except (OSError, subprocess.CalledProcessError) as e:
        return False

def get_pid(name):
    return int(check_output(['pidof','-s',name]))

@app.route('/error', methods=['GET','POST'])
def error_action():
    return render_template('reply_error.xml')

if __name__ == '__main__':
    open('playlist.txt', 'w').close()
    fo = open('autoplay.txt', 'w')
    fo.write('0')
    fo.close()
    app.run(host='0.0.0.0', port=80)

