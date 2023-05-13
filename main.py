from flask import Flask, render_template, request
import requests
import json
import clases.tiempo as date

app = Flask(__name__, template_folder="src")
r= requests.get('https://www.el-tiempo.net/api/json/v2/home')
data = r.json()
dato= date.DataJSON()
dato.ficheroJSON(data)
@app.route("/", methods=['GET'])
def elements():
    return render_template("index.html")
    
@app.route("/Tiempo", methods=['POST'])
def ciudad():
    value= request.form['ciudad']
    valorMax=dato.TemperaturaMax(value,data)
    valorMin= dato.TemperaturaMin(value,data)
    return render_template("temperatura.html", provincia=value,temperaturaMin=valorMin, temperaturaMax=valorMax )

@app.route("/", methods=['POST'])
def menuPrincipal():
    return render_template("index.html")   

    

if __name__=='__main__':
    app.run(debug=True)