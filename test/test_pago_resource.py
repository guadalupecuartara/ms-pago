import unittest
from app import create_app, db
from app.models.pago import Pago
from app.services.ms_pago import PagoService

class PagoResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_pago(self):
        client = self.app.test_client(use_cookies=True)
        response = client.post(
            "/api/v1/pago",
            json={"producto_id": 1, "precio": 100.0, "medio_pago": "tarjeta"},
        )
        self.assertEqual(response.status_code, 201)

    def test_obtener_pago(self):
        # Primero, crea un pago
        servicio_pago = PagoService()
        nuevo_pago = servicio_pago.crear_pago(producto_id=1, precio=100.0, medio_pago='tarjeta')

        client = self.app.test_client(use_cookies=True)
        response = client.get(f"/api/v1/pago/{nuevo_pago.producto_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["producto_id"], 1)
        self.assertEqual(response.json["precio"], 100.0)
        self.assertEqual(response.json["medio_pago"], "tarjeta")

if __name__ == "__main__":
    unittest.main()