import csv

from flask import Flask, render_template, request

app = Flask(__name__)

def salvar_dados(nome, email):
    with open('dados.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, email])

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        salvar_dados(nome, email)
        return f'Nome: {nome}, Email: {email}'

if __name__ == '__main__':
    app.run(debug=True)
