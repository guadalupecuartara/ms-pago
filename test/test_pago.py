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
        """Prueba la creación de un nuevo pago."""
        # Suponiendo que tienes un modelo `Pago`
        nuevo_pago = {
            'producto_id': 1,
            'precio': 100,
            'medio_pago': 'tarjeta'
        }

         # Inserta el pago en la base de datos usando SQL crudo
        db.session.execute(
            text("INSERT INTO pago (producto_id, precio, medio_pago) VALUES (:producto_id, :precio, :medio_pago)"),
            nuevo_pago
        )
        db.session.commit()

        # Verifica que el pago se haya creado correctamente
        result = db.session.execute(text("SELECT * FROM pago WHERE producto_id = 1")).fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result.producto_id, 1)
        self.assertEqual(result.precio, 100.0)
        self.assertEqual(result.medio_pago, 'tarjeta')

        
    def test_invalid_pago(self):
        """Prueba la creación de un pago con datos inválidos."""
        with self.assertRaises(ValueError):  # Espera que se lance ValueError por el precio negativo
            nuevo_pago = Pago(producto_id=1, precio=-50.0, medio_pago='tarjeta')
            db.session.add(nuevo_pago)
            db.session.commit()
        
    

if __name__ == '__main__':
    unittest.main()


"""
import os
import unittest
from sqlalchemy import text
from app import create_app, db

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
        Prueba la creación de un nuevo pago.
        # Suponiendo que tienes un modelo `Pago`
        nuevo_pago = {
            'producto_id': 1,
            'precio': 100,
            'medio_pago': 'tarjeta'
        }

        # Inserta el pago en la base de datos
        db.session.execute(
            text("INSERT INTO pago (producto_id, precio, medio_pago) VALUES (:producto_id, :precio, :medio_pago)"),
            nuevo_pago
        )
        db.session.commit()

        # Verifica que el pago se haya creado correctamente
        result = db.session.execute(text("SELECT * FROM pago WHERE producto_id = 1")).fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result.producto_id, 1)
        self.assertEqual(result.precio, 100)
        self.assertEqual(result.medio_pago, 'tarjeta')

    def test_invalid_pago(self):
        Prueba la creación de un pago con datos inválidos.
        # Suponiendo que `precio` no puede ser negativo
        pago_invalido = {
            'producto_id': 1,
            'precio': -50.0,  # Precio negativo debería fallar
            'medio_pago': 'tarjeta'
        }

        with self.assertRaises(Exception):  # Ajusta según cómo manejes los errores
            db.session.execute(
                text("INSERT INTO pago (producto_id, precio, medio_pago) VALUES (:producto_id, :precio, :medio_pago)"),
                pago_invalido
            )
            db.session.commit()

if __name__ == '__main__':
    unittest.main()
"""