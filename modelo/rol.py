from app import bd
from datetime import datetime


class Rol(bd.Model):
    __tablename__ = 'rol' #Nombre de la tabla
    idRol = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    rolNombre = bd.Column(bd.String(30), nullable=False)

    def __repr__(self):
        return f'{self.rolNombre}'
