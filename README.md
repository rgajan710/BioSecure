# BioSecure ID System

A biometric identification system for identifying unconscious individuals during emergencies using multi-modal biometric fusion (face, fingerprint, and iris).

## Features

- Multi-modal biometric identification
- Face recognition using face_recognition library
- Fingerprint matching using ORB features
- Iris recognition using pattern matching
- Fusion logic (2 out of 3 match required)
- PostgreSQL database for storing patient records
- RESTful API endpoints
- Docker support

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and update the values
3. Build and run using Docker:
   ```bash
   docker-compose up --build
   ```

Or run locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Initialize the database using `database/init.sql`
3. Run the application:
   ```bash
   flask run
   ```

## API Endpoints

- POST `/register` - Register new patient with biometric data
- POST `/identify` - Identify patient using biometric inputs
- POST `/manual-register` - Manual patient registration
- GET `/admin/patients` - List all patients
- DELETE `/admin/patient/<id>` - Delete patient record

## Testing

Run the test suite:
```bash
python -m unittest discover tests
```

## License

MIT License