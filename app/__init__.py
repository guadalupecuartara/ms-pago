from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config
from app.route import RouteMainApp

db = SQLAlchemy()

def create_app() -> Flask:
    app_context = os.getenv("FLASK_CONTEXT")
    app = Flask(__name__)

    f = config.factory(app_context)
    app.config.from_object(f)
    db.init_app(app)
    
    route = RouteMainApp()
    route.init_app(app)
    
    with app.app_context():
        db.create_all()  # Crear todas las tablas definidas en los modelos
    
    #@app.route('/')
    #def index():
     #   return jsonify({"message": "Bienvenido a la API de ms-pago!"})

    return app