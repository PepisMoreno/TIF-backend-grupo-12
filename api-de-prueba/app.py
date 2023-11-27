from flask import Flask, render_template, request 
#No me toma flaskext.mysql
# from flasketc.mysql import MySQL

#request sirve para recolectar la data que viene del formulario
app = Flask(__name__)
mysql = Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


