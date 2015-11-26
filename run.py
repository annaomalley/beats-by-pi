from flask import Flask, request, render_template
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
    if body == "#stop":
        subprocess("echo 0 > autoplay.txt", shell=True)
        os.system('pkill vlc')
    elif body == "#play":
        subprocess.Popen("python play.py", shell=True)
    elif body[0:2] == "#q":
        body = body[2:]
        cmd = "echo %s >> playlist.txt" % body
        subprocess.Popen(cmd, shell=True)
    elif body[0] == "#":
        subprocess.Popen("echo [Raspberry] Error: Invalid Command", shell=True)
        raise ValueError("Invalid Command")
    else:  
        with open('current_song.txt', 'w') as songfile:
            songfile.write(body)
        url = youtube_search.search(body)
        subprocess("echo 0 > autoplay.txt", shell=True)
        os.system('pkill vlc')
        print(url)
        cmd = "youtube-dl -f 140 -o - " + url + "| vlc-wrapper --play-and-exit --novideo --intf dummy -; python play.py"
        subprocess.Popen(cmd, shell=True)
    return "success"

@app.route('/error', methods=['GET','POST'])
def error_action():
    return render_template('reply_error.xml')


if __name__ == '__main__':
    subprocess.Popen("> playlist.txt; echo 1 > autoplay.txt", shell=True)
    app.run(host='0.0.0.0', port=80)
