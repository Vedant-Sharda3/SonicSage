from flask import Flask, jsonify, request
from Backend.Playlist import play_song, player
from Backend.downloader import download_by_name
from Backend.Search import search_video_url_by_title


app = Flask(__name__)
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!!</p>"

#CLI: $set FLASK_APP = Frontend-new\Hello.py
#CLI: $env:FLASK_APP = "Hello.py"

@app.route("/play", methods=["POST"])
def play_son():
    song = request.json["song"]
    print(song)
    play_song(song)
    return f"<p>Playing {song}</p>"

@app.route("/plays")
def play_sons():
    song = 'Roar'
    print(song)
    play_song(song)
    return f"<p>Playing</p>"


@app.route("/player", methods=["POST"])
def player_option():
    choice = request.json['choice']
    print(choice)
    player(choice)
    return f"<p>Player</p>"
#codepen.com - playground


@app.route("/download", methods=["POST"])
def download_song():
    name = request.json['name']
    title = download_by_name(name)
    return f"<p>Downloaded {title}</p>"


if __name__ == "__main__":
    app.run(debug=True)