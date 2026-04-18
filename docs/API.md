# API interna (lógica de negocio)

## `logic/auth.py`
- `hash_password(raw_password)`
- `verify_password(raw_password, password_hash)`
- `authenticate_user(session, username, password)`
- `set_new_password(session, user, new_password)`
- `SessionState` para timeout de sesión

## `logic/patient_manager.py`
- `create_patient(actor_id, payload)`
- `update_patient(actor_id, patient_id, payload)`
- `soft_delete_patient(actor_id, patient_id)`
- `search_patients(query, status)`

## `logic/appointment_manager.py`
- `schedule_appointment(actor_id, patient_id, when, reason)`
- `list_calendar(start, end)`

## `logic/report_generator.py`
- `generate_patient_pdf(patient, filename)`
- `export_patients_excel(patients, filename)`
