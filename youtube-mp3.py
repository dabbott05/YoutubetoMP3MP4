import yt_dlp # Used to download the videos
import os # Used to make directories and add files to local device
import re # Used to remove the illegal characters in the file title

def download_video(youtube_url, title, file_format):
    output_path = "musicDownloads" # Makes directory in current folder
    os.makedirs(output_path, exist_ok=True)

    title = re.sub(r'[\/:*?"<>|]', '', title) # No illegals!
    if file_format == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/{title}',
            'writethumbnail': True, # Downloads thumbnail onto the actual mp3 file
            'postprocessors': [
                {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', # Convert to MP3
                'preferredquality': '192', # Set bitrate
            },
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail'},  # Embeds thumbnail in MP3
            ],
            
        }
    else:
        ydl_opts = {
        'format': 'bv*[vcodec^=avc1]+ba[acodec^=mp4a]/b[ext=mp4]/best', # prioritizes H.264 + AAC (for Quicktime Player), but falls back to other formats if necessary
        'outtmpl': f'{output_path}/{title}.mp4',  # Forces MP4 extension
        'merge_output_format': 'mp4',  # Ensures final file is MP4
        'writethumbnail': True,  # Downloads thumbnail
        'postprocessors': [
            {'key': 'FFmpegMetadata'},  # Adds metadata
            {'key': 'EmbedThumbnail'},  # Embed thumbnail
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        filename = f"{output_path}/{title}.{file_format}"
        print(f"Downloaded {file_format.upper()}: {filename}")

# User inputs
video_url = input("Enter YouTube URL: ") 
custom_title = input("Name your file (no extension): ") 
custom_codec = input("Enter codec (mp3 or mp4): ")
while custom_codec not in ["mp3", "mp4"]:
    custom_codec = input("Enter codec (mp3 or mp4): ") 

download_video(video_url, custom_title, custom_codec) # Calls function
