from app import bd
from datetime import datetime


class Solicitud(bd.Model):
    __tablename__ = 'solicitudes' #Nombre de la tabla
    idSolicitud = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    idTipoSolicitud = bd.Column(bd.Integer, bd.ForeignKey('idTipoSolicitud.tiposolicitud'), nullable=False)
    idOficina = bd.Column(bd.Integer, bd.ForeignKey('idOficina.oficinas'), nullable=False)
    solCodigo = bd.Column(bd.String(50),nullable=False)
    solFechaRegistro = bd.Column(bd.DateTime, default=datetime.now(), nullable=False)
    solAnexo = bd.Column(bd.String(300),nullable=False)
    solEstado = bd.Column(bd.String(20),default="Solicitada", nullable=False)
    idRespuestaSol = bd.Column(bd.Integer, bd.ForeignKey('idRespuestaSol.respuestasolicitud'), nullable=False)

    def __repr__(self):
        return f'{self.usuLogin}'


