# admin.py
from app.services import database

def get_all_patients():
    """
    Retrieve all patient records for administration.
    """
    try:
        patients = database.get_all_patients()
        return {"status": "success", "patients": patients}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def delete_patient(patient_id):
    """
    Delete patient record by ID.
    """
    try:
        database.delete_patient(patient_id)
        return {"status": "success", "message": f"Patient {patient_id} deleted."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
