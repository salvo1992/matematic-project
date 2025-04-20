from flask import Flask, jsonify, request
from prettytable import PrettyTable

app = Flask(__name__)

# Funzione per il menu
def menu():
    table = PrettyTable(["No", "Menu"])
    table.add_row(["1", "Barisan Aritmatika"])
    table.add_row(["2", "Jika info suku hanya 2"])
    table.add_row(["3", "Deret Aritmatika"])
    return table.get_string()

# Endpoint per il menu
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return menu()

# Funzione per calcolare Barisan Aritmatika
@app.route('/api/aritmatika1', methods=['POST'])
def calculate_aritmatika1():
    data = request.json
    Un = data['suku-n']
    a = data['suku-pertama']
    b = data['beda']
    
    hasilakhir = a + (Un - 1) * b
    return jsonify({'hasil': hasilakhir})

# Funzione per calcolare Jika info suku hanya 2
@app.route('/api/aritmatika2', methods=['POST'])
def calculate_aritmatika2():
    data = request.json
    info1 = data['suku-n1']
    info2 = data['suku-n2']
    hasil1 = data['nilai-u1']
    hasil2 = data['nilai-u2']
    
    nb = hasil2 - hasil1
    i21 = (info2 - 1) - (info1 - 1)
    nilaib = nb / i21
    nilaia = hasil1 - (info1 - 1) * nilaib
    
    return jsonify({'nilai-a': nilaia, 'nilai-b': nilaib})

# Funzione per calcolare Deret Aritmatika
@app.route('/api/aritmatika3', methods=['POST'])
def calculate_aritmatika3():
    data = request.json
    Sn = data['jumlah-n']
    a = data['suku-pertama']
    b = data['beda']
    
    nilaiakhir = (Sn / 2) * (2 * a + (Sn - 1) * b)
    return jsonify({'jumlah': nilaiakhir})

if __name__ == '__main__':
    app.run(debug=True)
