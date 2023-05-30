# This is a sample Python script.
import os

import cv2
from numpy import save, load

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from util.imageutils import getFaces


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    path = r'C:\Users\varun\Desktop\VS\ph'
    list = getFaces(path)
    print("total faces are")
    print(len(list))
    print(type(list))
    save('faces.npy', list)
    print("File is saved successfully")
    newlist = load('faces.npy')
    for f in newlist:
        cv2.imshow('Resized Face', f)
        cv2.waitKey(0)
    if (list == newlist):
        print("Both are equal")
    else:
        print("ye sb kya h")
