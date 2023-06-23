from flask import Flask, jsonify, request
from Backend.Playlist import play_song, player


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

@app.route("/player", methods=["POST"])
def player_option():
    choice = request.json['choice']
    print(choice)
    player(choice)
    return f"<p>Player</p>"
#codepen.com - playground


if __name__ == "__main__":
    app.run(debug=False)