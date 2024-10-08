import os
import unittest
from sqlalchemy import text
from app import create_app, db
from app.models.pago import Pago 

class PagoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_create_pago(self):
         #"""Prueba la creación de un pago exitosamente."""
        nuevo_pago = Pago.crear_pago(producto_id=1, precio=100.0, medio_pago='Tarjeta')
        self.assertIsNotNone(nuevo_pago)
        self.assertEqual(nuevo_pago.producto_id, 1)
        self.assertEqual(nuevo_pago.precio, 100.0)
        self.assertEqual(nuevo_pago.medio_pago, 'Tarjeta')

        # Verificar que esté en la base de datos
        pagos_en_db = Pago.obtener_todos_los_pagos()
        self.assertEqual(len(pagos_en_db), 1)
  
    def test_crear_pago_precio_negativo(self):
        """Prueba la creación de un pago con un precio negativo (debería fallar)."""
        with self.assertRaises(ValueError):
            Pago.crear_pago(producto_id=1, precio=-50.0, medio_pago='Tarjeta')

        # Verificar que no haya ningún pago creado
        pagos_en_db = Pago.obtener_todos_los_pagos()
        self.assertEqual(len(pagos_en_db), 0)

    def test_crear_pago_medio_pago_largo(self):
        """Prueba la creación de un pago con un medio de pago que excede los 50 caracteres (debería fallar)."""
        with self.assertRaises(ValueError):
            Pago.crear_pago(producto_id=1, precio=100.0, medio_pago='T' * 51)  # Más de 50 caracteres

        # Verificar que no haya ningún pago creado
        pagos_en_db = Pago.obtener_todos_los_pagos()
        self.assertEqual(len(pagos_en_db), 0)

    def test_obtener_todos_los_pagos(self):
        """Prueba la obtención de todos los pagos."""
        Pago.crear_pago(producto_id=1, precio=100.0, medio_pago='Tarjeta')
        Pago.crear_pago(producto_id=2, precio=200.0, medio_pago='Efectivo')

        pagos = Pago.obtener_todos_los_pagos()
        self.assertEqual(len(pagos), 2)
        self.assertEqual(pagos[0].producto_id, 1)
        self.assertEqual(pagos[1].producto_id, 2)
   
if __name__ == '__main__':
    unittest.main()