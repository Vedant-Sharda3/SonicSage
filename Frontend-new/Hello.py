import time

from flask import Flask, jsonify, request
from Backend.Playlist import player, createCSV, delete_song, queue_song, likeSong
from Backend.PlaylistThread import playlist_player, get_curr, play_song, playlist_player_shuffled, \
    playlist_player_liked, playlist_player_shuffled_liked
from Backend.downloader import download_by_name
from Backend.Search import search_video_title
from Backend.Main import mic
import pandas as pd
from flask_cors import CORS  # cross_origin



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


@app.route("/likedplaylist")
def play_songs_liked():
    playlist_player_liked()
    return {"haha" : "Hello"}


@app.route("/queue", methods=["POST"])
def queue():
    song = request.json["song"].replace('/', '').replace('|', '').replace(':', '').replace('"', '').replace('-', '')
    print(song)
    check = queue_song(song)
    if check == 0:
        return jsonify({"Queued": f"{song}"})
    else:
        title = download_by_name(song)
        print(f"Downloaded {title}")
        check = queue_song(song)
        return jsonify({"Queued": f"Downloaded {song}"})

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


@app.route("/like")
def like_son():
    song = get_curr()
    print(song)
    check = likeSong(song)
    return jsonify({"Liked": f"{song}"})


@app.route("/playlistshuffle")
def play_songs_shuffle():
    playlist_player_shuffled()
    return {"haha" : "Hello"}


@app.route("/likedplaylistshuffle")
def play_songs_shuffle_liked():
    playlist_player_shuffled_liked()
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


@app.route("/micro")
def micro():
    song = mic()
    check = play_song(song)
    if check == 0:
        return jsonify({"Playing": f"{song}"})
    else:
        title = download_by_name(song)
        print(f"Downloaded {title}")
        check = play_song(song)
        return jsonify({"Playing": f"Downloaded {song}"})




if __name__ == "__main__":
    createCSV()
    app.run(debug=True)