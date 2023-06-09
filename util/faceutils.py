import cv2
from keras_facenet import FaceNet
from mtcnn import MTCNN
import os
from numpy import expand_dims
from util.imageutils import is_image
from sklearn.metrics.pairwise import cosine_similarity

facenet_model = '20170511-185253'
similarity_threshold = 0.75
def get_faces(path):
    print("images to be extracted from " + path)
    faces = []
    for rootDir, dirs, files in os.walk(path):
        for file in files:
            img_file = os.path.join(rootDir, file)
            if is_image(img_file):
                faces_from_image = get_faces_from_image(img_file)
                faces = faces + faces_from_image
                if len(faces) > 10:
                    return faces
    return faces


def get_faces_from_image(image):
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
    except Exception:
        print(Exception)
        print("ok")
        print(image)

    return faces

def getFacenet():
    model = FaceNet(key=facenet_model)
    return model

def get_face_signatures(model,faces):
    return get_face_signature_util(model, faces)



def get_face_signature_util(model, faces):
    face_signatures = []
    for face in faces:
        face = face.astype('float32')
        # standardize pixel values across channels (global)
        mean, std = face.mean(), face.std()
        face = (face - mean) / std
        # transform face into one sample
        sample = expand_dims(face, axis=0)
        # make prediction to get embedding
        prediction = model.embeddings(sample)
        face_signatures.append(prediction)
    return face_signatures

def getImageFacesMapping(path):
    print(" Image-Faces to be extracted from " + path)
    imageFacesMap = {}
    model = getFacenet()
    for rootDir, dirs, files in os.walk(path):
        for file in files:
            img_file = os.path.join(rootDir, file)
            if is_image(img_file):
                faces_from_image = get_faces_from_image(img_file)
                faceSign = get_face_signatures(model,faces_from_image)
                imageFacesMap[img_file] = faces_from_image
    return imageFacesMap


def getImageFacesEmbeddingsMapping(path):
    print(" Image-Faces_Embeddings to be extracted from " + path)
    imageFacesEmbeddingsMap = {}
    model = getFacenet()
    images = 0
    for rootDir, dirs, files in os.walk(path):
        for file in files:
            img_file = os.path.join(rootDir, file)
            if is_image(img_file):
                images = images + 1
                print("processing file no: "+str(images)+" "+str(img_file))
                faces_from_image = get_faces_from_image(img_file)
                face_embedding = get_face_signatures(model,faces_from_image)
                imageFacesEmbeddingsMap[img_file] = face_embedding
    return imageFacesEmbeddingsMap

def faceEmdbeddingsAsList(path):
    face_embeddings_test = getImageFacesEmbeddingsMapping(path)
    emdbeddings = []
    for key in face_embeddings_test:
        print("printing key in get face embedding :"+key)
        print(type(face_embeddings_test[key]))
        emdbeddings = emdbeddings + face_embeddings_test[key]
    return emdbeddings


def is_eligible(test_face, saved_faces):
    for face in saved_faces:
        print("computed similarity:")
        similarity = cosine_similarity(test_face,face)
        print(similarity)
        if similarity[0][0] >= similarity_threshold:
            return True
    return False