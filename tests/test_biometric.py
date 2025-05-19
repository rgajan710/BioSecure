import unittest
from app.services import face, fingerprint, iris, fusion
from app.logic import register, identify, manual_entry
import os
import json

class TestBiometricSystem(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = "tests/test_data"
        if not os.path.exists(self.test_data_dir):
            os.makedirs(self.test_data_dir)
        
    def test_face_recognition(self):
        test_image = os.path.join(self.test_data_dir, "test_face.jpg")
        result = face.extract_face_encoding(test_image)
        self.assertIsNotNone(result)
        
    def test_fingerprint_matching(self):
        test_image = os.path.join(self.test_data_dir, "test_fingerprint.jpg")
        features = fingerprint.extract_fingerprint_features(test_image)
        self.assertIsNotNone(features)
        
    def test_iris_recognition(self):
        test_image = os.path.join(self.test_data_dir, "test_iris.jpg")
        features = iris.extract_iris_features(test_image)
        self.assertIsNotNone(features)
        
    def test_fusion_logic(self):
        result = fusion.fusion_match(True, True, False)
        self.assertTrue(result)
        result = fusion.fusion_match(False, False, True)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()