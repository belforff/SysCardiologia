import unittest

from logic.validators import validate_patient_payload


class ValidatorTests(unittest.TestCase):
    def test_validate_patient_payload_and_bmi(self):
        payload = {
            "first_name": "Ana",
            "last_name": "Pérez",
            "age": 40,
            "gender": "F",
            "email": "ana@example.com",
            "phone": "+1 555-222-1111",
            "blood_pressure": "120/80",
            "weight_kg": 70,
            "height_m": 1.7,
        }
        result = validate_patient_payload(payload)
        self.assertEqual(result["bmi"], 24.22)

    def test_invalid_email_raises(self):
        payload = {
            "first_name": "Ana",
            "last_name": "Pérez",
            "age": 40,
            "gender": "F",
            "email": "ana-example.com",
        }
        with self.assertRaises(ValueError):
            validate_patient_payload(payload)


if __name__ == "__main__":
    unittest.main()
