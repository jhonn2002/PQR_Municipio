from app import bd
from datetime import datetime


class ResSolicitud(bd.Model):
    __tablename__ = 'respuestasolicitud' #Nombre de la tabla
    idRespuestaSol = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    resFechaRespuesta = bd.Column(bd.DateTime, default=datetime.now(), nullable=False)
    resAnexo = bd.Column(bd.String(300),nullable=False)

    def __repr__(self):
        return f'{self.resFechaSolicitud}'
