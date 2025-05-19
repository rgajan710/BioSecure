# preprocessing.py

import cv2
import numpy as np

def resize_image(image, size=(256, 256)):
    return cv2.resize(image, size)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def normalize(image):
    return cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

def preprocess(image, target_size=(256, 256)):
    """Full pipeline: resize, grayscale, normalize."""
    image = resize_image(image, target_size)
    image = grayscale(image)
    image = normalize(image)
    return image
