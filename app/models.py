# app/models.py
from . import db

class Calopisita(db.Model):
    __tablename__ = 'calopistas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    mutacao = db.Column(db.String(100), nullable=False)

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
