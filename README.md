# Python Video Downloader

## Prerequisites
[x] ffmpeg
[x] python-ffmpeg (pip install python-ffmpeg)

## How to use
You can download a video using the URL of the video or manifest and its destination or you can create a text file with all the videos and their destinations.

### 1. URL Mode
1. Write u and press Enter.
2. Write the video/manifest URL and press Enter.
3. Write the name of the file and press Enter.
4. The download of the video starts instantly.

### 2. File Mode
Create a text file containing une download per line with the format 'url destination' (url and destination separated by a space)

1. Write f and press Enter.
2. Write the path of the file and press Enter.
3. The download of the first video starts instantly, at the end of each download the next one will start instantly.

Write q and press Enter to quit.

## Sharepoint info
You can download videos from Microsoft Sharepoint. To do so:
1. Open your browser developers tools and select tab network.
2. Open your video or refresh the page.
3. Search for 'videomanifest'.
4. Copy the url of the video manifest and use it to download the video.

##
Use this script at your own risk. Any usage of this script is your responsability.
