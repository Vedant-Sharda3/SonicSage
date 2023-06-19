import os
from downloader import download
from Search import search_video_url_by_title
from speech_text import convert_wav_to_text
from Audio_Recorder import record_audio


def main():
    print("What would you like to download today? Speak now...")
    # Record the Audio
    duration = 6  # Duration in seconds
    filename = "recorded_audio.wav"
    record_audio(duration, filename)
    print(f"Audio recorded for {duration} seconds and saved as {filename}")

    # Read the Instruction
    wav_file_path = "recorded_audio.wav"
    result = convert_wav_to_text(wav_file_path)
    print(result)
    os.remove('recorded_audio.wav')

    download(search_video_url_by_title(result))


if __name__ == '__main__':
    main()
