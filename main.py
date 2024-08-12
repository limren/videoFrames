import sys
import os
import cv2
import random 
# --- Args
# 0 :
# 1 : source directory/file - must be a valid path - must be a directory containing videos or a file which is a video.
# 2 : destination directory  - must be a valid path.
# 3 : offset of frames - optional.

# -------- Don't be worried about having files that doesn't have a video extension - it will ignore them.


def checkSourceExists(path):
    if(not os.path.exists(path)):
        print("The given source directory path doesn't exists.")
        sys.exit()
        
def getFramesFromVideo(videoPath, destPath, offset = 20):
    checkSourceExists(videoPath)
    video = cv2.VideoCapture(videoPath)

    # Count the number of frames | offset of a certain amount of frames
    frames = 0

    # While the video still have frames to read
    while video.isOpened():

        isImageExtracted, image = video.read()

        if(isImageExtracted):
            randomNumber = random.randint(0, 20000) 
            randomNumber2 = random.randint(20000, 40000) 
            cv2.imwrite(f"{destPath}/frames_{frames}_{randomNumber}_{randomNumber2}.jpg", image)
            # Allow to skip offset frames
            frames += offset
            video.set(cv2.CAP_PROP_POS_FRAMES, frames)
        else:
            video.release()
            break


nbArgs = len(sys.argv)
args = sys.argv

if(nbArgs < 3):
    print("The program ", args[0], "requires at least 2 args")
    sys.exit()

sourcePath = args[1]
destPath = args[2]
offset = 20
if(nbArgs >= 4):
    offset = int(args[3])
checkSourceExists(sourcePath)

sourceIsDirectory = os.path.isdir(sourcePath)

if(sourceIsDirectory):
    dirList = os.listdir(sourcePath)
    for file in dirList:
        filePath = sourcePath + file
        getFramesFromVideo(filePath, destPath, offset)
else:
    getFramesFromVideo(sourcePath, destPath, offset)



