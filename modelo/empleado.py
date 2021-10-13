from app import bd

class Empleado(bd.Model):
    __tablename__ = 'empleados' #Nombre de la tabla
    idEmpleado = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    idPersona = bd.Column(bd.Integer, bd.ForeignKey('idPersona.personas'), nullable=False)
    idOficina = bd.Column(bd.Integer, bd.ForeignKey('idOficina.oficinas'), nullable=False)
    
    def __repr__(self):
        return f'{self.idPersona}'




