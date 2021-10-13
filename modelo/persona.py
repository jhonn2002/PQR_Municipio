from app import bd

class Persona(bd.Model):
    __tablename__ = 'personas' #Nombre de la tabla
    idPersona = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    perDocumento = bd.Column(bd.Integer, nullable=False)
    perNombres = bd.Column(bd.String(50),nullable=False)
    perApellidos = bd.Column(bd.String(50),nullable=False)
    perCorreo = bd.Column(bd.String(50),nullable=False)
    perGenero = bd.Column(bd.String(20), nullable=False)

    def __repr__(self):
        return f'{self.perNombres}'


