"""  
    This module will handle the encoding of facial images into a format that can be used for recognition. 
    Typically, this involves extracting facial features and converting them into a numerical representation (vector).
"""
import numpy as np
import cv2
import dlib
from imutils import face_utils
from imutils.face_utils import *

def encode_face(image, face_detector, face_encoder):
    """
    This function takes an image as input and returns the encoded facial features.
    :param image: The input image containing a face
    :param face_detector: The face detector model
    :param face_encoder: The face encoder model
    :return: The encoded facial features
    """
    # Detect faces in the image
    faces = face_detector(image, 1)
    if len(faces) == 0:
        return None

    # Assume only one face in the image
    face = faces[0]
    # Get the facial landmarks
    shape = face_encoder.get_landmarks(image, face)
    # Encode the facial features
    encoding = face_encoder.get_encoding(image, shape)
    return encoding

def compare_faces(encoding1, encoding2, threshold=0.6):
    """
    This function compares two sets of facial features and returns whether they match.
    :param encoding1: The first set of facial features
    :param encoding2: The second set of facial features
    :param threshold: The threshold for considering a match
    :return: True if the faces match, False otherwise
    """
    distance = np.linalg.norm(encoding1 - encoding2)
    return distance <= threshold    
