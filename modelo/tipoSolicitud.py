from app import bd

class TipoSolicitud(bd.Model):
    __tablename__ = 'tiposolicitud' #Nombre de la tabla
    idTipoSolicitud = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    tipoSolicitud = bd.Column(bd.String(30),nullable=False)
    

    def __repr__(self):
        return f'{self.tipoSolicitud}'




