# app/routes.py
from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Calopisita, Usuarios

@app.route("/")
def HomePage():
    return render_template("homepage.html")

@app.route("/calopsita", methods=["GET", "POST"])  # Adicionando 'POST' aqui
def index():
    if request.method == "POST":
        # Lógica para lidar com o login
        nome = request.form['nome']
        senha = request.form['senha']
        
        # Aqui você deve verificar se o usuário existe e se a senha está correta
        # Exemplo de verificação (isso é apenas um exemplo, você deve substituir por sua lógica)
        usuario = Usuarios.query.filter_by(nome=nome).first()
        if usuario and usuario.senha == senha:  # Verifica se a senha está correta
            flash(f'Bem-vindo, {nome}!', 'success')
            return redirect(url_for('dashboard'))  # Redireciona para a página inicial após login
        else:
            flash('Nome de usuário ou senha incorretos', 'error')

    return render_template("index.html")


@app.route("/cadastrar-calopsita", methods=["POST"])
def CadastrarCalopisita():
    nome = request.form['nome']
    sexo = request.form['sexo']
    idade = request.form['idade']
    mutacao = request.form['mutacao']

    nova_calopisita = Calopisita(nome=nome, sexo=sexo, idade=int(idade), mutacao=mutacao)

    db.session.add(nova_calopisita)
    db.session.commit()

    flash(f"Calopsita {nome} cadastrada com sucesso!")
    return redirect(url_for('index'))

@app.route("/cadastrar-usuario", methods=['GET', 'POST'])
def CadastrarUsuarios():
    if request.method == "POST":
        nome = request.form['nome']
        senha = request.form['senha']
        email = request.form['email']
        usuario_existente = Usuarios.query.filter_by(email=email).first()

        if usuario_existente:
            flash('Usuário já cadastrado com este email!', "error")
            return redirect(url_for('index'))

        novo_usuario = Usuarios(nome=nome, senha=senha, email=email)

        db.session.add(novo_usuario)
        db.session.commit()

        flash(f'Usuário {nome} cadastrado com sucesso!', "sucesso")
        return redirect(url_for('index'))

    return render_template('cadastrar_usuario.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')