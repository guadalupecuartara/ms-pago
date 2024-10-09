import unittest
from app import create_app, db
from app.models.pago import Pago 
from app.services.ms_pago import PagoService
from app.repositories.pago_repository import PagoRepository

class PagoTestCase(unittest.TestCase):
    def setUp(self):
        """Configura el entorno para las pruebas."""
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Limpia el entorno después de las pruebas."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_pago(self):
        """Prueba la creación de un pago."""
        servicio_pago = PagoService()
        nuevo_pago = servicio_pago.crear_pago(producto_id=1, precio=100.0, medio_pago='tarjeta')
        self.assertEqual(nuevo_pago.producto_id, 1)
        self.assertEqual(nuevo_pago.precio, 100.0)
        self.assertEqual(nuevo_pago.medio_pago, 'tarjeta')
        self.assertIsNotNone(nuevo_pago.fecha_pago)  # Verifica que la fecha de pago no sea None

    def test_obtener_todos_los_pagos(self):
        """Prueba la obtención de todos los pagos."""
        servicio_pago = PagoService()
        servicio_pago.crear_pago(producto_id=1, precio=100.0, medio_pago='tarjeta')
        servicio_pago.crear_pago(producto_id=2, precio=150.0, medio_pago='efectivo')
        
        pagos = servicio_pago.obtener_todos_los_pagos()
        self.assertEqual(len(pagos), 2)  # Verifica que se hayan creado dos pagos

    def test_precio_negativo(self):
        """Prueba que no se pueda crear un pago con precio negativo."""
        servicio_pago = PagoService()
        with self.assertRaises(ValueError):
            servicio_pago.crear_pago(producto_id=1, precio=-50.0, medio_pago='tarjeta')

if __name__ == '__main__':
    unittest.main()