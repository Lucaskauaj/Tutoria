from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.LargeBinary)
    role = db.Column(db.String(10), default="USER")

class RefreshToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
