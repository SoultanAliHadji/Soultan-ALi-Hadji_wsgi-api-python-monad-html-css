from flask import Flask, render_template, request, url_for
import requests
import json
from py_monad import *

#serializing request-json-html
app = Flask(__name__)

@app.route('/')
def home():
    covid19=requests.get("https://data.covid19.go.id/public/api/prov.json")
    data=covid19.json()
    isi=data['list_data']
    return render_template('index.html',isi=isi, len=len(isi))

@app.route('/tabel')
def tabel():
    covid19=requests.get("https://data.covid19.go.id/public/api/prov.json")
    data=covid19.json()
    isi=data['list_data']
    return render_template('tabel.html',isi=isi, len=len(isi))

@app.route('/pymonad', methods=['POST', 'GET'])
def pymonad():
    if request.method=='POST':
        bil1=request.form['bil1']
        bil2=request.form['bil2']
        pilihan=request.form['pilihan']
        if pilihan=='penjumlahan':
            opsi=penjumlahan(int(bil1), int(bil2))
        elif pilihan=='pengurangan':
            opsi=pengurangan(int(bil1), int(bil2))
        elif pilihan=='perkalian':
            opsi=perkalian(int(bil1), int(bil2))
        elif pilihan=='pembagian':
            opsi=pembagian(int(bil1), int(bil2))
        elif pilihan=='multiplication':
            opsi=(((multiplication1(int(bil1))*2)+(multiplication2(int(bil2))*2))/2)
        return render_template('py_monad.html', opsi=opsi)
    else:
        return render_template('py_monad.html')
    
if __name__ == "__main__":
    app.run(debug=True)