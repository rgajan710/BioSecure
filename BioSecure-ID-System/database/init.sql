CREATE TABLE IF NOT EXISTS patients (
    patient_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    contact VARCHAR,
    face_encoding JSON,
    fingerprint_features JSON,
    iris_features JSON
);
