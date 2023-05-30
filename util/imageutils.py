import os
from PIL import Image
import cv2
from mtcnn import MTCNN
def getFaces(path):
    print("images to be extracted from "+path)
    faces = []
    for rootDir,dirs,files in os.walk(path):
        for file in files:
            imgFile = os.path.join(rootDir,file)
            if isImage(imgFile):
                facesFromImage = getFacesFromAnImage(imgFile)
                faces = faces + facesFromImage
                if(len(faces)>10):
                    return faces
    return faces

def isImage(file):
    try:
        img = Image.open(file)
        img.verify()  # Additional check to verify the image file integrity
        return True
    except (IOError, SyntaxError):
        return False

def getFacesFromAnImage(image):
    faces = []

    image = cv2.imread(image)

    # Create an MTCNN detector
    detector = MTCNN()

    # Detect faces in the image
    try:
        results = detector.detect_faces(image)

        # Iterate over the detected faces
        for result in results:
            # Extract the coordinates of the bounding box
            x, y, width, height = result['box']

            # Crop the face region from the image
            face = image[y:y + height, x:x + width]

            # Resize the face to 160x160 pixels
            resized_face = cv2.resize(face, (160, 160))
            faces.append(resized_face)
    except(Exception):
        print(Exception)
        print("ok")
        print(image)

    return faces