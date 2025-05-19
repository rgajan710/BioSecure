# identify.py
from app.services import face, fingerprint, iris, fusion, database

def identify_patient(face_file, fingerprint_file, iris_file):
    """
    Identify patient by matching biometric inputs against database.
    Uses fusion logic: match if 2 out of 3 biometrics match.
    """
    try:
        face_encoding = face.get_face_encoding(face_file)
        fingerprint_encoding = fingerprint.get_fingerprint_encoding(fingerprint_file)
        iris_encoding = iris.get_iris_encoding(iris_file)

        # Match against database records
        face_match = database.match_face(face_encoding)
        fingerprint_match = database.match_fingerprint(fingerprint_encoding)
        iris_match = database.match_iris(iris_encoding)

        matched = fusion.fusion_match(face_match, fingerprint_match, iris_match)
        if matched:
            patient_data = database.get_patient_by_biometrics(face_encoding, fingerprint_encoding, iris_encoding)
            return {"status": "success", "patient_data": patient_data}
        else:
            return {"status": "fail", "message": "No matching patient found"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
