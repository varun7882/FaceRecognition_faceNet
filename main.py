# This is a sample Python script.
import os
import pickle
import shutil
from datetime import datetime

from util.faceutils import getImageFacesEmbeddingsMapping, faceEmdbeddingsAsList, is_eligible
from util.imageutils import getImages

dataDir = r'data'
dataDir2 = r'C:\Users\varun\Desktop\VS\savedFaceData'
savedDataFile = 'img_faces_embeddings_data.pkl'
savedWeddingDataFile = 'img_faces_embeddings_wedding_data.pkl'
savedWeddingDataFile2 = 'img_faces_embeddings_wedding_data2.pkl'
savedWeddingDataFile3 = 'img_faces_embeddings_wedding_data3.pkl'
savedWeddingDataFile4 = 'img_faces_embeddings_wedding_data4.pkl'
savedWeddingDataFile5 = 'img_faces_embeddings_wedding_data5.pkl'
sourceTestDir = r'C:\Users\varun\Desktop\VS\photosToMatch'
targetResultDir = r'C:\Users\varun\Desktop\VS\relevant_images'
allImagespath1 = r'C:\Users\varun\Desktop\VS\all_images'
allImagespath2 = r'C:\Users\varun\Desktop\VS\all_images2'
allImagespath3 = r'C:\Users\varun\Desktop\VS\all_images3'
allImagespath4 = r'C:\Users\varun\Desktop\VS\all_images4'
allImagespath5 = r'C:\Users\varun\Desktop\VS\all_images5'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def save_image_faces_embeddings_mappings(imagesPath,saveInFile):
    start_time = datetime.now()
    face_embeddings = getImageFacesEmbeddingsMapping(imagesPath)
    print("total about to be saved files are")
    print(len(face_embeddings))
    print(type(face_embeddings))
    if not os.path.exists(dataDir2):
        os.mkdir(dataDir2)
    with open(os.path.join(dataDir2,saveInFile), 'wb') as file:
        pickle.dump(face_embeddings, file)
    print("File is saved successfully")
    print("time taken in saving: " + str(datetime.now() - start_time))

def load_image_faces_embeddings_mappings(loadFromFile):
    with open(os.path.join(dataDir2, loadFromFile), 'rb') as file:
        face_embeddings = pickle.load(file)
    print("total loaded faces are")
    print(len(face_embeddings))
    print(type(face_embeddings))
    return face_embeddings

def extract_relevant_images(sourceTestDir,targetResultDir):
    start_time = datetime.now()
    test_face_embeddings = faceEmdbeddingsAsList(sourceTestDir)
    face_embeddings = load_image_faces_embeddings_mappings(savedWeddingDataFile)
    face_embeddings.update(load_image_faces_embeddings_mappings(savedWeddingDataFile2))
    face_embeddings.update(load_image_faces_embeddings_mappings(savedWeddingDataFile3))
    face_embeddings.update(load_image_faces_embeddings_mappings(savedWeddingDataFile4))
    face_embeddings.update(load_image_faces_embeddings_mappings(savedWeddingDataFile5))
    imagesExtracted = save_relevant_images(test_face_embeddings,face_embeddings,targetResultDir)
    print("Relevant images extracted successfully: " + str(imagesExtracted))
    print("time taken in extraction " + str(datetime.now() - start_time))

def save_relevant_images(test_faces,face_embeddings,targetResultDir):
    if os.path.exists(targetResultDir):
        shutil.rmtree(targetResultDir)
    os.makedirs(targetResultDir)
    totalImages = 0
    i = 0
    for img_name in list(face_embeddings.keys()):
        i = i + 1
        print("Checking in image no:"+str(i)+" with name: "+img_name)
        for test_face in test_faces:
            if is_eligible(test_face,face_embeddings[img_name]):
                totalImages = totalImages + 1
                shutil.copy2(img_name,targetResultDir)
                break
    return totalImages

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Varun, welcome to facenet program')
    #save_image_faces_embeddings_mappings(allImagespath5,savedWeddingDataFile5)
    extract_relevant_images(sourceTestDir,targetResultDir)

# to be called to extract images
#getImages(r'F:\Varun\Sakshi X Varun')


