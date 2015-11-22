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
        os.system('pkill vlc')
    else:  
        with open('current_song.txt', 'w') as songfile:
            songfile.write(body)
        url = youtube_search.search(body)
        os.system('pkill vlc')
        print(url)
        cmd = "youtube-dl -o - " + url + "| vlc-wrapper -"
        subprocess.Popen(cmd, shell=True)
    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
