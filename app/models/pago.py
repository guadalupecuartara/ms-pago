from app import db
from sqlalchemy.orm import validates

class Pago(db.Model):
    __tablename__ = 'pago'
    
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    medio_pago = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Pago {self.id}>'
    
    @validates('precio')
    def validate_precio(self, key, value):
        """Valida que el precio no sea negativo."""
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        return value

    @validates('medio_pago')
    def validate_medio_pago(self, key, value):
        """Valida y limpia el campo medio_pago."""
        if len(value) > 50:
            raise ValueError("El medio de pago no puede exceder los 50 caracteres.")
        return value.strip()  # Elimina espacios en blanco alrededor del valor
