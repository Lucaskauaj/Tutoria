from flask import Flask
from models import db
from routes.auth import auth
from routes.usuarios import usuarios
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    from models import Usuario, RefreshToken

    app.register_blueprint(auth)
    app.register_blueprint(usuarios)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
