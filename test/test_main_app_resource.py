import os
import unittest
from sqlalchemy import text
from app import create_app, db
class MainAppResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_ms_pago(self):
        client = self.app.test_client(use_cookies=True)
        response = client.get("http://localhost:5000/api/v1/pago")
        self.assertEqual(response.status_code, 200)
    def test_ms_pago_crear(self):
        client = self.app.test_client(use_cookies=True)
        response = client.post(
            "http://localhost:5000/api/v1/pago",
            json={"producto_id": 1, "precio": 100.0, "medio_pago": "tarjeta"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_ms_obtener_todos_los_pagos(self):
        client = self.app.test_client(use_cookies=True)
        client.post(
            "http://localhost:5000/api/v1/pago",
            json={"producto_id": 1, "precio": 100.0, "medio_pago": "tarjeta"},
        )
        client.post(
            "http://localhost:5000/api/v1/pago",
            json={"producto_id": 2, "precio": 150.0, "medio_pago": "efectivo"},
        )
        response = client.get("/api/v1/pago/todos")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.get_json()["pagos"]), 0)
if __name__ == "__main__":
    unittest.main()