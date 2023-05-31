# This is a sample Python script.
import os

import cv2
from numpy import save, load
from util.faceutils import get_faces
from util.faceutils import get_face_signatures


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Varun, welcome to facenet program')
    #save_faces()
    faces_from_file = load(r'data\faces_data.npy')
    for f in faces_from_file:
        cv2.imshow('Resized Face', f)
    print("faces count")
    print(len(faces_from_file))
    face_signatures = get_face_signatures(faces_from_file)
    print(type(face_signatures))
    print(len(face_signatures))
    print(type(face_signatures[0]))
    print(repr(face_signatures[0]))
    print(face_signatures[0].shape)