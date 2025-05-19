# app/services/face.py
import face_recognition

def extract_face_encoding(image_path):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        return encodings[0].tolist()
    return None

def match_face(test_image_path, stored_encoding):
    test_image = face_recognition.load_image_file(test_image_path)
    test_encoding = face_recognition.face_encodings(test_image)
    if test_encoding and stored_encoding:
        result = face_recognition.compare_faces([stored_encoding], test_encoding[0])
        return result[0]
    return False
