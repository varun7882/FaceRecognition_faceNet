# This is a sample Python script.
import os
import pickle

import cv2
import numpy
from numpy import save, load
from util.faceutils import get_faces, getImageFacesMapping, getFacenet
from util.faceutils import get_face_signatures
from util.imageutils import getImages


dataDir = r'data'
dataDir2 = r'C:\Users\varun\Desktop\VS\test_dataset'
savedDataFile = 'img_faces_data.pkl'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def save_faces():
    path = r'C:\Users\varun\Desktop\VS\ph'
    faces = get_faces(path)
    print("total faces are")
    print(len(faces))
    print(type(faces))
    dataDir = "data"
    save(os.path.join(dataDir,"faces_data"),faces)
    print("File is saved successfully")


def load_faces():
    faces_from_file = load(r'data\faces_data.npy')
    for f in faces_from_file:
        cv2.imshow('Resized Face', f)
    print("faces count")
    print(len(faces_from_file))
    return faces_from_file



def save_image_faces_mappings():
    imagesPath = r'C:\Users\varun\Desktop\VS\ph'
    facesMap = getImageFacesMapping(imagesPath)
    print("total faces are")
    print(len(facesMap))
    print(type(facesMap))
    os.mkdir(dataDir2)
    for key in facesMap:
        print(type(facesMap[key]))
        print(type(facesMap[key][0]))
        break
    with open(os.path.join(dataDir2,savedDataFile), 'wb') as file:
        pickle.dump(facesMap, file)
    print("File is saved successfully")


def load_image_faces_map():
    with open(os.path.join(dataDir2,savedDataFile), 'rb') as file:
        faces_from_file = pickle.load(file)
    print("faces count")
    print(len(faces_from_file))
    print(type(faces_from_file))
    print(faces_from_file)
    for key in faces_from_file:
        print(key)
        print(len(faces_from_file[key]))
    return faces_from_file

def save_face_embeddings(image_face_map):
    image_signature_map = {}
    model = getFacenet()
    for img in image_face_map:
        print(img)
        print(type(image_face_map[img]))
        face_embeddings = get_face_signatures(model,numpy.asarray(image_face_map[img]))
        image_signature_map[img] = face_embeddings
    with open(os.path.join(dataDir,"faceSignatures.pkl"), 'wb') as file:
        pickle.dump(image_signature_map, file)
    print("File is saved successfully")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Varun, welcome to facenet program')
    getImages(r'F:\Varun\Sakshi X Varun')


