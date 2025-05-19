from app.services import face, fingerprint, iris, database
import uuid

def register_patient(face_path, fingerprint_path, iris_path, patient_info):
    try:
        face_encoding = face.extract_face_encoding(face_path)
        fingerprint_features = fingerprint.extract_fingerprint_features(fingerprint_path)
        iris_features = iris.extract_iris_features(iris_path)

        patient_data = {
            "patient_id": str(uuid.uuid4()),
            "name": patient_info["name"],
            "contact": patient_info["contact"],
            "biometrics": {
                "face": face_encoding,
                "fingerprint": fingerprint_features,
                "iris": iris_features
            }
        }

        database.save_patient_data(patient_data)
        return {"status": "success", "patient_id": patient_data["patient_id"]}

    except Exception as e:
        return {"status": "error", "message": str(e)}
