# SonicSage

### What is it?
An automated playlist generator, which sources music free of cost, generates a playlist and incorporates voice control. It isn't limited to music, but can get you ebooks, videos, or anything off YouTube. 

### Easy Mods
If you want to download the videos instead of just audio, edit downloader.py to get the video instead of just the audio-stream.


### Coming soon
We are working on creating a WebApp in React, but until it's complete, you will need to run Main.py to download songs, which will be saved in songs_mp3. 
*Since adding a functional microphone in React is a little tricky, this may take a minute.

### Don't worry
PyTube's cipher.py has a bug so don't worry if you get a regx match error - hold on - we're not the only ones with this problem!

This link should help us track the progress of the issue: https://github.com/pytube/pytube/issues/1678

Our current fix involves editing cipher.py to replace the list function_patterns in get_throttling_function_name() with:
``function_patterns = [
        # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
        # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
        # var Bpa = [iha];
        # ...
        # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
        # Bpa.length || iha("")) }};
        # In the above case, `iha` is the relevant function name
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',]``
### Until Next Time
Happy Listening:)