from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder='public', template_folder='templates')
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "DB_Floreria"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('Fl.html')


@app.route('/Flores.html')
def Preguntas():
    return render_template('Flores.html')

@app.route('/Guardar', methods = ['POST'])
def Guardar():
    if request.method == 'POST':
        VP1 = request.form['Pregunta1']
        VP2 = request.form['Pregunta2']
        VP3 = request.form['Pregunta3']
        Ho = mysql.connection.cursor()
        Ho.execute('insert into tbFlores(nombre, cantidad, precio) values (%s, %s, %s)',(VP1,VP2,VP3))
        mysql.connection.commit()
    return render_template(url_for('Flores'))



if __name__=='__main__':
    app.run(port= 9005, debug=True)
