# app/services/iris.py
import cv2
import numpy as np

def extract_iris_features(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (224, 224))  # Standardize size
    return img.flatten().tolist()

def match_iris(test_img_path, stored_features):
    if stored_features is None:
        return False
    test_img = cv2.imread(test_img_path, cv2.IMREAD_GRAYSCALE)
    test_img = cv2.resize(test_img, (224, 224))
    test_features = test_img.flatten()
    stored = np.array(stored_features)
    diff = np.linalg.norm(test_features - stored)
    return diff < 8000  # Threshold can be tuned
