from flask import Flask, jsonify, request
from Backend.Playlist import player, createCSV, delete_song
from Backend.PlaylistThread import playlist_player, get_curr, play_song, playlist_player_shuffled
from Backend.downloader import download_by_name
from Backend.Search import search_video_title
import pandas as pd
from flask_cors import CORS  # , cross_origin


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
    check = play_song(song)
    if check == 0:
        return jsonify({"Playing": f"{song}"})
    else:
        title = download_by_name(song)
        print(f"Downloaded {title}")
        check = play_song(song)
        return jsonify({"Playing": f"Downloaded {song}"})

# The below API is just a tester for postman. Do not delete!
@app.route("/playlist")
def play_songs():
    playlist_player()
    return {"haha" : "Hello"}


@app.route("/delete", methods=["POST"])
def del_son():
    song = request.json["song"]
    print(song)
    check = delete_song(song)
    if check == 0:
        print(1)
        return jsonify({"Deleted": f"{song}"})
    else:
        print(2)
        song = get_curr()
        print(song)
        if song == '':
            print('No song provided')
            return jsonify({"Deleted": "Nothing"})
        player("u")
        check = delete_song(song)
        player("r")
        return jsonify({"Deleted": f"Currently Playing {song}"})


@app.route("/playlistshuffle")
def play_songs_shuffle():
    playlist_player_shuffled()
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
    print(name)
    title = search_video_title(name)
    print(title)
    return {"title": title}


@app.route("/current", methods=["GET"])
def get_playing():
    current = get_curr()
    return {"current": f"{current.replace('Lyrics', '').replace('Music', '').replace('(', '').replace(')', '').replace('Video', '').replace('Official', '')}"}


@app.route("/table", methods=["GET"])
def get_JSON_playlist():
    table = pd.read_csv("C:/Users/athar/PycharmProjects/SonicSage/Backend/song_names.csv")
    print(table)
    JSON_data = table.to_json()
    print(JSON_data)
    return JSON_data


if __name__ == "__main__":
    createCSV()
    app.run(debug=True)