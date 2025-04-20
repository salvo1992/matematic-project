// Funzioni per mostrare le diverse sezioni del contenuto
function mostraTermineN() {
    document.getElementById('content').innerHTML = `
        <h2>Calcolo del termine n-esimo</h2>
        <form id="aritmetica1Form">
            <label for="suku-n">Inserisci il numero del termine (n):</label>
            <input type="number" id="suku-n" name="suku-n" required><br><br>
            
            <label for="suku-pertama">Inserisci il primo termine (a):</label>
            <input type="number" id="suku-pertama" name="suku-pertama" required><br><br>
            
            <label for="beda">Inserisci la differenza tra i termini (b):</label>
            <input type="number" id="beda" name="beda" required><br><br>
            
            <button type="button" onclick="calcolaTermineN()">Calcola</button>
        </form>
        <div id="resultAritmatika1"></div>
    `;
}

function mostraDaDueTermini() {
    document.getElementById('content').innerHTML = `
        <h2>Calcolo con due termini noti</h2>
        <form id="aritmetica2Form">
            <label for="suku-n1">Numero del primo termine (n₁):</label>
            <input type="number" id="suku-n1" name="suku-n1" required><br><br>
            
            <label for="suku-n2">Numero del secondo termine (n₂):</label>
            <input type="number" id="suku-n2" name="suku-n2" required><br><br>
            
            <label for="nilai-u1">Valore del primo termine (U₁):</label>
            <input type="number" id="nilai-u1" name="nilai-u1" required><br><br>
            
            <label for="nilai-u2">Valore del secondo termine (U₂):</label>
            <input type="number" id="nilai-u2" name="nilai-u2" required><br><br>
            
            <button type="button" onclick="calcolaDaDueTermini()">Calcola</button>
        </form>
        <div id="resultAritmatika2"></div>
    `;
}

function mostraSommaN() {
    document.getElementById('content').innerHTML = `
        <h2>Somma dei primi n termini</h2>
        <form id="aritmetica3Form">
            <label for="jumlah-n">Inserisci il numero di termini (n):</label>
            <input type="number" id="jumlah-n" name="jumlah-n" required><br><br>
            
            <label for="suku-pertama">Inserisci il primo termine (a):</label>
            <input type="number" id="suku-pertama" name="suku-pertama" required><br><br>
            
            <label for="beda">Inserisci la differenza tra i termini (b):</label>
            <input type="number" id="beda" name="beda" required><br><br>
            
            <button type="button" onclick="calcolaSomma()">Calcola</button>
        </form>
        <div id="resultAritmatika3"></div>
    `;
}

// Funzioni per calcolare i risultati e mostrarli
async function calcolaTermineN() {
    const sukuN = document.getElementById('suku-n').value;
    const sukuPertama = document.getElementById('suku-pertama').value;
    const beda = document.getElementById('beda').value;

    const response = await fetch('/api/aritmatika1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'suku-n': sukuN,
            'suku-pertama': sukuPertama,
            'beda': beda
        }),
    });

    const data = await response.json();
    document.getElementById('resultAritmatika1').innerText = `Il termine numero ${sukuN} è: ${data.hasil}`;
}

async function calcolaDaDueTermini() {
    const sukuN1 = document.getElementById('suku-n1').value;
    const sukuN2 = document.getElementById('suku-n2').value;
    const nilaiU1 = document.getElementById('nilai-u1').value;
    const nilaiU2 = document.getElementById('nilai-u2').value;

    const response = await fetch('/api/aritmatika2', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'suku-n1': sukuN1,
            'suku-n2': sukuN2,
            'nilai-u1': nilaiU1,
            'nilai-u2': nilaiU2
        }),
    });

    const data = await response.json();
    document.getElementById('resultAritmatika2').innerText = `a = ${data['nilai-a']}, b = ${data['nilai-b']}`;
}

async function calcolaSomma() {
    const jumlahN = document.getElementById('jumlah-n').value;
    const sukuPertama = document.getElementById('suku-pertama').value;
    const beda = document.getElementById('beda').value;

    const response = await fetch('/api/aritmatika3', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'jumlah-n': jumlahN,
            'suku-pertama': sukuPertama,
            'beda': beda
        }),
    });

    const data = await response.json();
    document.getElementById('resultAritmatika3').innerText = `La somma dei primi ${jumlahN} termini è: ${data.jumlah}`;
}

