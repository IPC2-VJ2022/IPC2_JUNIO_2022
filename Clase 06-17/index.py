#pip install flask
from flask import Flask,request,render_template
import xml.etree.ElementTree as ET
import json
import re

#App va a ser nuestra varianble para crear las rutas POST GET
app=Flask(__name__)

#Definimos nuestra ruta inicial
@app.route('/')
def inicio():
    return 'Pantalla de inicio IPC2'

#Definimos una ruta GET
@app.route('/ruta1')
def ruta1():
    cadena=""
    cadena+="{"+"\n"
    cadena+="\"datos\": \"mensaje de prueba\""+"\n"
    cadena+="}"
    #objeto json para guardar la info
    objJson=json.loads(cadena)
    return objJson



#METODO PRINCIPAL
if(__name__=='__main__'):
    app.run(host="0.0.0.0",port=9000,debug=False)
