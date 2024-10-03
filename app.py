from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'segredo'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cadastro_eleitor', methods=['GET', 'POST'])
def cadastro_eleitor():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        zona = request.form['zona']

        

    return render_template('cadastro_eleitor.html')


@app.route('/cadastro_candidato', methods=['GET', 'POST'])
def cadastro_candidato():
    if request.method == 'POST':
        nome = request.form['nome']
        partido = request.form['partido']
        idade = request.form['idade']
        endereco = request.form['endereco']
        rg = request.form['rg']

        if int(idade) < 0:
            flash("A idade não pode ser negativa!")
            return redirect(url_for('cadastro_candidato'))

        flash("Cadastro de Candidato realizado com sucesso!")
        return redirect(url_for('confirmacao'))

    return render_template('cadastro_candidato.html')

@app.route('/cadastro_partido', methods=['GET', 'POST'])
def cadastro_partido():
    if request.method == 'POST':
        numero = request.form['numero']
        sigla = request.form['sigla']
        nome = request.form['nome']
        cidade = request.form['cidade']
        uf = request.form['uf']

        flash("Cadastro de Partido realizado com sucesso!")
        return redirect(url_for('confirmacao'))

    return render_template('cadastro_partido.html')


@app.route('/cadastro_local', methods=['GET', 'POST'])
def cadastro_local():
    if request.method == 'POST':
        zona = request.form['zona']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        uf = request.form['uf']

        flash("Cadastro de Local de Votação realizado com sucesso!")
        return redirect(url_for('confirmacao'))

    return render_template('cadastro_local.html')


@app.route('/cadastro_mesario', methods=['GET', 'POST'])
def cadastro_mesario():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        cpf = request.form['cpf']

        try:
            datetime.strptime(data_nascimento, '%Y-%m-%d')
        except ValueError:
            flash("A data de nascimento deve estar no formato YYYY-MM-DD!")
            return redirect(url_for('cadastro_mesario'))

        flash("Cadastro de Mesário realizado com sucesso!")
        return redirect(url_for('confirmacao'))

    return render_template('cadastro_mesario.html')


@app.route('/confirmacao')
def confirmacao():
    return render_template('confirmacao.html')

if __name__ == '_main_':
    app.run(debug=True)