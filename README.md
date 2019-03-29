# GratefulDeadDownloader (~);}
A python script for downloading Grateful Dead shows from archive.org. 

The script will download all songs from a given show URL, fetch and embed song metadata, and generate and embed custom album artwork.

# Usage
```
$ python gdDownload.py <Show URL> <Download Location>

```
### Show URL
The URL of any recording on archive.org
Example: https://archive.org/details/gd1977-05-08.mtx.dan.35086.flac24

### Download Location
The Location on your computer where the songs will be downloaded.
```#ALBUM```- will be replaced with the show name.
```#ARTIST```- will be replaced with the artist name.
Example: ```/home/user/Music/#ARTIST/#ALBUM/```
(Directories will be created if they don’t already exist)

# Artwork Customization

To change the appearance of the generated album artwork replace: “background.png”(Image) and/or “default.ttf”(Font) with an image/font of your choosing. Make sure the file names stay the same.

# Dependencies 

python 
pprint
urllib
json
pillow
eyed3

To install required python packages use ```pip install <package-name>```





