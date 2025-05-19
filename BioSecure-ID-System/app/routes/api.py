from flask import Flask, request, jsonify
from app.logic import register, identify, manual_entry, admin
import io

app = Flask(__name__)

# ---------- Registration Endpoint ----------
@app.route('/register', methods=['POST'])
def register_patient():
    try:
        face_file = request.files['face']
        fingerprint_file = request.files['fingerprint']
        iris_file = request.files['iris']

        face_stream = io.BytesIO(face_file.read())
        fingerprint_stream = io.BytesIO(fingerprint_file.read())
        iris_stream = io.BytesIO(iris_file.read())

        patient_info = request.form.to_dict()

        response = register.register_patient(
            face_stream, fingerprint_stream, iris_stream, patient_info
        )
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ---------- Identification Endpoint ----------
@app.route('/identify', methods=['POST'])
def identify_patient():
    try:
        face_file = request.files['face']
        fingerprint_file = request.files['fingerprint']
        iris_file = request.files['iris']

        face_stream = io.BytesIO(face_file.read())
        fingerprint_stream = io.BytesIO(fingerprint_file.read())
        iris_stream = io.BytesIO(iris_file.read())

        response = identify.identify_patient(
            face_stream, fingerprint_stream, iris_stream
        )
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ---------- Manual Entry Endpoint ----------
@app.route('/manual-register', methods=['POST'])
def manual_register():
    try:
        patient_info = request.json
        response = manual_entry.manual_register(patient_info)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ---------- Admin: Get All Patients ----------
@app.route('/admin/patients', methods=['GET'])
def list_all_patients():
    try:
        response = admin.get_all_patients()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ---------- Admin: Delete a Patient ----------
@app.route('/admin/patient/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        response = admin.delete_patient(patient_id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ---------- Run App ----------
if __name__ == '__main__':
    app.run(debug=True)
