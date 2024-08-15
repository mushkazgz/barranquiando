from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/barrancos/gorgas-de-fuentes-callejas')
def gorgas_de_fuentes_callejas():
    return render_template('barranco_gorgas_de_fuentes_callejas.html')

@app.route('/barrancos/barranco-de-sierra-helada')
def barranco_de_sierra_helada():
    return render_template('barranco_sierra_helada.html')

@app.route('/barrancos/barranco-de-orbisa')
def barranco_de_orbisa():
    return render_template('barranco_orbisa.html')

# Otras rutas aquí...

if __name__ == '__main__':
    app.run(debug=True)
