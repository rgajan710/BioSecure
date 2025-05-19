# manual_entry.py

from app.services import database

def manual_register(patient_info):
    """
    Register patient manually without biometric data.
    """
    try:
        patient_data = {
            "patient_id": patient_info.get("patient_id"),
            "name": patient_info.get("name"),
            "contact": patient_info.get("contact"),
            "biometrics": {
                "face": None,
                "fingerprint": None,
                "iris": None
            }
        }
        database.save_patient_data(patient_data)
        return {"status": "success", "message": "Patient registered manually"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
