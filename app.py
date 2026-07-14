from flask import Flask
from routes.dashboard import dashboard
from routes.api import api
from routes.reportes import reportes_bp

from utils.camera_manager import camera_manager

def create_app():

    app = Flask(__name__)
    app.camera_manager = camera_manager
    app.register_blueprint(dashboard)
    app.register_blueprint(api)
    app.register_blueprint(reportes_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False
    )