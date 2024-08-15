# web/app.py

from flask import Flask, render_template, abort
from mongoengine import connect
from models.barranco import Barranco

app = Flask(__name__)

connect(db='barranquiando_db', host='localhost', port=27017)

@app.route('/')
def home():
    barrancos = Barranco.objects()
    return render_template('home.html', barrancos=barrancos)

@app.route('/barrancos/<nombre>')
def barranco_detalle(nombre):
    # Usar first() para obtener el primer resultado o None si no existe
    barranco = Barranco.objects(nombre=nombre).first()
    if barranco is None:
        abort(404)  # Lanzar un error 404 si no se encuentra el barranco
    return render_template('barranco_detalle.html', barranco=barranco)

if __name__ == '__main__':
    app.run(debug=True)
