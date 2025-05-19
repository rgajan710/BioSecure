# app/services/fingerprint.py
import cv2
import numpy as np

orb = cv2.ORB_create()

def extract_fingerprint_features(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    keypoints, descriptors = orb.detectAndCompute(img, None)
    return descriptors.tolist() if descriptors is not None else None

def match_fingerprint(test_img_path, stored_descriptors):
    if stored_descriptors is None:
        return False
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    test_img = cv2.imread(test_img_path, cv2.IMREAD_GRAYSCALE)
    keypoints, descriptors = orb.detectAndCompute(test_img, None)
    if descriptors is None:
        return False
    matches = bf.match(np.array(descriptors, dtype=np.uint8), np.array(stored_descriptors, dtype=np.uint8))
    return len(matches) > 20  # Threshold can be tuned
