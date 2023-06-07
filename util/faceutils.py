import cv2
from keras.saving.saving_api import load_model
from keras_facenet import FaceNet
from mtcnn import MTCNN
import os
from numpy import expand_dims
from util.imageutils import is_image

facenet_model = '20170511-185253'
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


def get_face_signatures(faces):
    model = FaceNet(key=facenet_model)
    #model = load_model('facenet_keras.h5')
    print('Loaded Model Facenet')
    #return get_face_signature_util(model, faces)
    return model.embeddings(faces)


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
    print("image-Faces to be extracted from " + path)
    imageFacesMap = {}
    for rootDir, dirs, files in os.walk(path):
        for file in files:
            img_file = os.path.join(rootDir, file)
            if is_image(img_file):
                faces_from_image = get_faces_from_image(img_file)
                imageFacesMap[img_file] = faces_from_image
                if len(imageFacesMap) > 10:
                    return imageFacesMap

