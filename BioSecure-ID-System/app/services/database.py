# app/services/database.py
import psycopg2
import json
import os

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "hospital_db",
    "user": "postgres",
    "password": "your_password"
}

def connect():
    return psycopg2.connect(**DB_CONFIG)

def save_patient_data(patient_data):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO patients (patient_id, name, contact, face_encoding, fingerprint_features, iris_features)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        patient_data["patient_id"],
        patient_data["name"],
        patient_data["contact"],
        json.dumps(patient_data["biometrics"]["face"]),
        json.dumps(patient_data["biometrics"]["fingerprint"]),
        json.dumps(patient_data["biometrics"]["iris"])
    ))
    conn.commit()
    cur.close()
    conn.close()

def load_all_patients():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT patient_id, name, contact, face_encoding, fingerprint_features, iris_features FROM patients")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    patients = []
    for row in rows:
        patients.append({
            "patient_id": row[0],
            "name": row[1],
            "contact": row[2],
            "biometrics": {
                "face": json.loads(row[3]) if row[3] else None,
                "fingerprint": json.loads(row[4]) if row[4] else None,
                "iris": json.loads(row[5]) if row[5] else None,
            }
        })
    return patients

def delete_patient_data(patient_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE patient_id = %s", (patient_id,))
    conn.commit()
    cur.close()
    conn.close()

def update_patient_data(patient_id, field, value):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"UPDATE patients SET {field} = %s WHERE patient_id = %s", (value, patient_id))
    conn.commit()
    cur.close()
    conn.close()
