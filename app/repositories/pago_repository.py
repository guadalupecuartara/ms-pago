from app import db
from app.models.pago import Pago

class PagoRepository:

    @staticmethod
    def crear_pago(producto_id, precio, medio_pago):
        nuevo_pago = Pago(producto_id=producto_id, precio=precio, medio_pago=medio_pago)
        db.session.add(nuevo_pago)
        db.session.commit()
        return nuevo_pago

    @staticmethod
    def obtener_pago_por_id(pago_id): #find_by_id
        return Pago.query.get(pago_id)
    
    @staticmethod
    def obtener_todos_los_pagos():  #find_all
        return Pago.query.all()

    @staticmethod
    def eliminar_pago(pago_id):
        pago = Pago.query.get(pago_id)
        if pago:
            db.session.delete(pago)
            db.session.commit()
