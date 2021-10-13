from app import bd

class Usuario(bd.Model):
    __tablename__ = 'usuarios' #Nombre de la tabla
    idUsuario = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    idRol = bd.Column(bd.Integer, bd.ForeignKey('idRol.rol'), nullable=False)
    idEmpleado = bd.Column(bd.Integer, bd.ForeignKey('idEmpleado.empleado'), nullable=False)
    usuLogin = bd.Column(bd.String(50),nullable=False)
    usuContraseña = bd.Column(bd.String(50),nullable=False)
    usuEstado = bd.Column(bd.String(20),default="Activo", nullable=False)

    def __repr__(self):
        return f'{self.usuLogin}'




