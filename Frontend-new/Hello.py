from flask import Flask, jsonify, request
from Backend.Playlist import play_song, player
from Backend.downloader import download_by_name
from Backend.Search import search_video_title
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

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
    return jsonify({"Playing": f"{song}"})

@app.route("/plays")
def play_sons():
    song = "Can't Say"
    print(song)
    play_song(song)
    return {"haha" : "Hello"}


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

@app.route("/title", methods=["POST"])
def get_title():
    name = request.json['name']
    title = search_video_title(name)
    return {"Title": title}


if __name__ == "__main__":
    app.run(debug=True)