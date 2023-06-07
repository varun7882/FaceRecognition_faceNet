import os
import shutil

from PIL import Image

imageDataDir = r'C:\Users\varun\Desktop\VS'
def is_image(file):
    try:
        img = Image.open(file)
        img.verify()  # Additional check to verify the image file integrity
        return True
    except (IOError, SyntaxError):
        return False

def getImages(source):
    print("images to be extracted from " + source)
    destinationFolder = "all_images"
    os.mkdir(os.path.join(imageDataDir,destinationFolder))
    imageCount = 0
    nonImageCount = 0
    nonImages = []
    for rootDir, dirs, files in os.walk(source):
        for file in files:
            img_file = os.path.join(rootDir, file)
            if is_image(img_file):
                imageCount = imageCount + 1
                print("saving image "+str(imageCount)+" with name "+img_file)
                shutil.copy2(img_file,os.path.join(imageDataDir,destinationFolder))
            else:
                nonImageCount = nonImageCount + 1
                nonImages.append(img_file)
    print("Images found "+str(imageCount))
    print("nonImages found "+str(nonImageCount))
    print(nonImages)

