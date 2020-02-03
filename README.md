# GratefulDeadDownloader (~);}
A python script for downloading Grateful Dead shows from archive.org.<br>

The script will download all songs from a given show URL, fetch and embed song metadata, and generate and embed custom album artwork.

# Usage
```
$ python gdDownload.py <Show URL> <Download Location>
```
### Show URL
The URL of any recording on archive.org<br>
Example: https://archive.org/details/gd1977-05-08.mtx.dan.35086.flac24

### Download Location
The Location on your computer where the songs will be downloaded.<br>
```#ALBUM```- will be replaced with the show name.<br>
```#ARTIST```- will be replaced with the artist name.<br>
Example: ```/home/user/Music/#ARTIST/#ALBUM/```<br>
(Directories will be created if they don’t already exist)<br>

# Artwork Customization

To change the appearance of the generated album artwork replace: “background.png”(Image) and/or “default.ttf”(Font) with an image/font of your choosing. Make sure the file names stay the same.

# Python Dependencies 

- wget
- pillow
- eyed3

To install required python packages use ```$ pip install <package-name>```

# Windows Users

If you are getting libmagic errors install python magic: ``` pip install python-magic-bin==0.4.14 ```






