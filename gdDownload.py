
import urllib.request, json
from pprint import pprint
from PIL import Image, ImageDraw, ImageFont
import os
import platform 
import sys
import eyed3
import wget


fileSep = '/'

def writeTextOnImage(startImage, fontFile, fontSize, locX, locY, color, message,outputImage):
    image = Image.open(startImage)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(fontFile, size=int(float(fontSize)))

    if locX == "center":
        textWidth = font.getsize(message)[0] #Get the pixel length (X) of message
        imageWidth = image.size[0] #Get the pixel width of the image

        locX = int((imageWidth / 2) - (textWidth / 2))

    if locY == "center":
        textHeight = font.getsize(message)[1] #Get the pixel length (Y) of message
        imageHeight = image.size[1] #Get the pixel height of the image

        locY = int((imageHeight / 2) - (textHeight / 2))


    (x, y) = (int(float(locX)), int(float(locY)))
    color = color
    draw.text((x, y), message, fill=color, font=font)

    image.save(outputImage)

def setAlbumArt(scanDir,key):
    keyArray = key.split(',')

    def getSubDirs(dirpath):
        dirArray = []
        for (dirpath, dirnames, filenames) in os.walk(dirpath):
            for f in filenames:
               dirArray.append(os.path.join(dirpath, f))

        return dirArray


    dirArray = (getSubDirs(scanDir))
    foundArt = []


    print("Searching for album art...")
    for f in dirArray:
        tmp = f[f.rfind(fileSep) + 1:]

        if tmp in keyArray:
            foundArt.append(f)
    print("done.")
    print("Found: " +str(len(foundArt)) + " albums: ")
    print(foundArt)

    for f in dirArray:
        for tmpArt in foundArt:
            if (tmpArt[:tmpArt.rfind(fileSep)] == f[:f.rfind(fileSep)]) and (f not in foundArt):
                if ".mp3" in f:
                    print("Embeding " + f)
                    audiofile = eyed3.load(f)
                    if (audiofile.tag == None):
                        audiofile.initTag()
                    encodeType = 'image/jpeg'
                    if ".png" in tmpArt:
                        encodeType = 'image/png'

                    audiofile.tag.images.set(3, open(tmpArt,'rb').read(), 'image/jpeg')
                    audiofile.tag.save()


def downloadShow(origURL,filePath):
    if filePath == "":
        filePath = "./"


    showURL = origURL + "&output=json"

    origURL = origURL.replace("details", "download")

    with urllib.request.urlopen(showURL) as url:
        data = json.loads(url.read().decode())


        year = data['metadata']['year'][0]
        date = data['metadata']['date'][0]
        print("Year: " + year)
        print("Date: " + date)




        jsonFiles = data['files']

        for fileName in jsonFiles:
            if ".mp3" in fileName:

                title = jsonFiles[fileName]["title"]
                track = jsonFiles[fileName]["track"]
                album = jsonFiles[fileName]["album"]
                artist = jsonFiles[fileName]["creator"]

                filePath = filePath.replace("#ARTIST", artist)
                filePath = filePath.replace("#ALBUM", album)

                title = title.replace("/", "")

                print(fileName)
                print("\tTitle: "+title)
                print("\tTrack: "+track)
                print("\tAlbum: "+album)
                print("\tArtist: "+artist)

                downloadURL = origURL + fileName

                print("Downloading: " + downloadURL)

                if not os.path.exists(filePath):
                    os.makedirs(filePath)

                if not os.path.exists(filePath + "cover.png"):
                    writeTextOnImage("background.png","default.ttf", "500", "center", "50", "white", artist, filePath + "cover.png")
                    writeTextOnImage(filePath + "cover.png","default.ttf", "500", "center", "2000", "white", date, filePath + "cover.png")

                try:
                   wget.download(downloadURL, filePath +  title.replace('->', '').replace('>', '') + '.mp3' )  

                except:
                    print("ERROR (1) A DOWNLOAD ERROR HAS OCCURED!")

                try:
                    audiofile = eyed3.load(filePath + title + ".mp3")
                    audiofile.tag.artist = artist
                    audiofile.tag.album = album
                    audiofile.tag.album_artist = artist
                    audiofile.tag.title = title
                    audiofile.tag.track_num = int(track)
                    audiofile.tag.save()
                except:
                    print("ERROR (2) A PARSE ERROR HAS OCCURED!")

                print("\n\n")
        setAlbumArt(filePath, "cover.png")


if(platform.system() == 'Windows'):
	print('Windows Detected! Setting file separator to \\')
	fileSep = '\\'
	
downloadShow(sys.argv[1],sys.argv[2])
