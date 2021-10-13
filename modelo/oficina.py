from app import bd

class Oficina(bd.Model):
    __tablename__ = 'oficinas' #Nombre de la tabla
    idOficina = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    ofiNombre = bd.Column(bd.String(30),nullable=False)
    

    def __repr__(self):
        return f'{self.ofiNombre}'




