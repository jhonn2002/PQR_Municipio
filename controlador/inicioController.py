from app import app
from flask import Flask, render_template, session

@app.route('/')
def inicio():
    return render_template('solicitud.html')

@app.route('/mostrarIniciarSesion')
def mostrarIniciarSesion():
    return render_template('frmIniciarSesion.html')
    
@app.route('/registrarse')
def mostrarRegistarse():
    return render_template('frmRegistrarse.html')
