from app import app
from modelo.usuario import *
from flask import Flask, request, render_template,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


@app.route("/iniciarSesion",methods=['POST'])
def iniciarSesion():
    login = request.form['txtUsuarioInicio']
    password=request.form['txtContraseñaInicio']
    print(login + password)
    if(login and password):
        try:
            usuario = Usuario.query.filter(Usuario.usuLogin==login).\
                    filter(Usuario.usuContraseña==password).first()
            if(usuario!=None):
                #se crea la variable de sesión
                session['user']=login
                print('Se inicio sesion')
                return render_template("empleado/index.html")
            else:
                mensaje="Credenciales de ingreso no validas"           
        except exc.SQLAlchemyError as ex:
            mensaje = str(ex)           
    else:
        mensaje="Faltan datos"        
    return render_template("frmIniciarSesion.html",mensaje=mensaje)


        