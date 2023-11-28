#Ult 27-11 Sofi
from flask import Flask, render_template, request 
#Sofi: No me toma flaskext.mysql, puse sólo flask
from flaskext.mysql import MySQL

#Sofi: request sirve para recolectar la data que viene del formulario
app = Flask(__name__)
#Sofi: InstanciaMySQL
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123' #aÑADIR CONTRASEÑA?
app.config['MYSQL_DATABASE_DB'] = 'plantas_bd'

#Sofi: Acá la inicializamos
mysql.init_app(app)

#Decorador
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")
#Sofi: para probar mysql 
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

#    sql="INSERT INTO `características` VALUES (1,'sin luz directa','mucha','suelo/roca/troncos','superficies porosas','-')"
    cursor.execute(mysql)

    conn.commit()

    return render_template('templates/index.html')




#Recordar: para correr app es python source/app.py
if __name__ == '__main__':
    app.run(debug=True)
    
