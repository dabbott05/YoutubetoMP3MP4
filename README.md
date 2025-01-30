# YouTube Video Downloader

#### This Python script allows you to download YouTube videos and convert them into either audio (MP3) or video (MP4) format. It allows you to specify a custom title for your file and automatically handles illegal characters in the file name. The program can also download and embed video thumbnails in MP3/MP4 files.

#### It is designed to be easy to use for downloading content directly from YouTube for offline use, with support for both audio and video files.

## Features


### MP3 Support: Downloads audio from YouTube videos and saves them in MP3 format with customizable bitrate (192 kbps).

### MP4 Support: Downloads video with H.264 video codec and AAC audio codec, saved as an MP4 file.

### Customizable File Names: Allows you to choose the title for the downloaded file (without illegal characters).

### Thumbnail Embedding: Downloads and embeds the video thumbnail in the MP3 or MP4 file.

### Directory Management: Automatically saves downloaded files in a musicDownloads directory in the current working folder.


## Requirements


Before running the script, make sure you have the following installed:

Python 3.x (Download and install from python.org)

yt-dlp: A powerful YouTube video downloader

ffmpeg: A tool for handling multimedia files (audio and video)

To install these dependencies, follow the instructions below:


#### Install yt-dlp

### Install the yt-dlp Python package using pip:

```pip install yt-dlp```


#### Install ffmpeg

You’ll need ffmpeg to handle audio and video post-processing. Follow the instructions for your operating system:

### macOS: Use Homebrew to install ffmpeg:

```brew install ffmpeg```

### Windows: Download ffmpeg from [here](https://ffmpeg.org/download.html) and follow the installation instructions.

### Linux: On Ubuntu/Debian-based systems, install ffmpeg using:

```sudo apt install ffmpeg```

## Instructions for Use

#### Clone or Download the Script:
You can clone or download the script to your local machine.

#### Run the Script: 
Open a terminal and navigate to the folder containing the script. Run the script using Python:
```python youtube_downloader.py```

#### Input Prompts: 
The script will prompt you for the following inputs:
Enter YouTube URL: Paste the URL of the YouTube video you wish to download.

#### Name your file (no extension): 
Enter the desired name for the downloaded file (without file extension). Illegal characters (like /:*?"<>|) will be automatically removed.

#### Enter codec (mp3 or mp4): 
Choose whether you want to download the file as an MP3 (audio) or MP4 (video).

#### Download and Save: 
The script will download the video/audio and save it in the musicDownloads folder in the current directory. The file will be named based on your input and the chosen format.

## Example Usage
```
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Name your file (no extension): RickRoll
Enter codec (mp3 or mp4): mp3
This will download the audio from the provided YouTube video as an MP3 file named RickRoll.mp3 and save it in the musicDownloads folder.
```


## Notes

The file name will have illegal characters removed, such as /:*?"<>|.

MP3 format will download only the audio of the video and convert it to MP3 at 192 kbps.

MP4 format will download both the best quality video and audio and save them as an MP4 file.

Thumbnails will be downloaded and embedded into the MP3/MP4 file.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
