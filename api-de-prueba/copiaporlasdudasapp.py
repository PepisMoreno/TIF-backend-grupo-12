from flask import Flask, render_template, request 
#request sirve para recolectar la data que viene del formulario
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route() #completar acá la ruta
def consulta():
    nombrePlanta = request.form('Nombre')
    consulta = request.form('consulta')
    #acá iria algo para usar esa data que me mando el usuario y buscar en la BD la respuesta que saldrá por ouput
    output= #acá va la respuesta que le damos al usuario, a su consulta. sacada de la BD no se como
    return #podriamos hacer con un if else, si el usuario pregunto por la luz o el agua o etc, le damos tal o cual respuesta.