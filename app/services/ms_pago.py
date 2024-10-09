from app.repositories.pago_repository import PagoRepository
from app.models import Pago
from datetime import datetime

class PagoService:
    def __init__(self):
        self.pago_repository = PagoRepository()
    
    def crear_pago(self,producto_id, precio, medio_pago):
        """crea un pago nuevo"""
        # Validación del precio
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        return self.pago_repository.crear_pago(producto_id, precio, medio_pago)

    def obtener_pago(self, producto_id):
        """Obtiene un pago específico por producto_id."""
        return self.pago_repository.obtener_pago_por_producto_id(producto_id)
    
    def obtener_todos_los_pagos(self):
        """Obtiene todos los pagos existentes."""
        return self.pago_repository.obtener_todos_los_pagos()