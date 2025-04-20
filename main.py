from flask import Flask, jsonify, request, render_template
from programma_sequenze_aritmetiche import (
    calcola_termine_n,
    calcola_da_due_termini,
    calcola_somma_n
)

app = Flask(__name__)

# Route per la pagina principale
@app.route('/')
def home():
    return render_template("index.html")  # index.html deve essere in /templates

# API per calcolare il termine n-esimo
@app.route('/api/aritmatika1', methods=['POST'])
def api_calcola_termine_n():
    data = request.json
    n = int(data['suku-n'])
    a = int(data['suku-pertama'])
    b = int(data['beda'])

    risultato = calcola_termine_n(n, a, b)
    return jsonify({'hasil': risultato})

# API per calcolare a e b da due termini noti
@app.route('/api/aritmatika2', methods=['POST'])
def api_calcola_da_due_termini():
    data = request.json
    n1 = int(data['suku-n1'])
    n2 = int(data['suku-n2'])
    u1 = int(data['nilai-u1'])
    u2 = int(data['nilai-u2'])

    risultato = calcola_da_due_termini(n1, n2, u1, u2)
    return jsonify(risultato)

# API per calcolare la somma dei primi n termini
@app.route('/api/aritmatika3', methods=['POST'])
def api_calcola_somma():
    data = request.json
    n = int(data['jumlah-n'])
    a = int(data['suku-pertama'])
    b = int(data['beda'])

    somma = calcola_somma_n(n, a, b)
    return jsonify({'jumlah': somma})

# Avvia il server
if __name__ == '__main__':
    app.run(debug=True)
