class RouteMainApp:
    def init_app(self, app):
        from app.resources.pago_resource import pago_bp
        app.register_blueprint(pago_bp, url_prefix="/api/v1")