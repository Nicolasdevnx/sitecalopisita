# app/routes.py
from flask import render_template, request, redirect, url_for, flash, jsonify
from . import app, db
from .models import Calopisita, Usuarios
from flask_login import login_required
from datetime import datetime

@app.route("/")
def HomePage():
    return render_template("homepage.html")

@app.route("/calopsita", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form['nome']
        senha = request.form['senha']
        
        usuario = Usuarios.query.filter_by(nome=nome).first()
        if usuario and usuario.senha == senha:
            flash(f'Bem-vindo, {nome}!', 'success')
            return redirect(url_for('dashboard'))
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
@login_required
def dashboard():
    try:
        calopsitas = Calopisita.query.order_by(Calopisita.id.desc()).limit(10).all()
        total_calopsitas = Calopisita.query.count()
        total_usuarios = Usuarios.query.count()

        return render_template('dashboard.html',
                             calopsitas=calopsitas,
                             total_calopsitas=total_calopsitas,
                             total_usuarios=total_usuarios)
    except Exception as e:
        return render_template('dashboard.html', 
                             error="Erro ao carregar o dashboard: " + str(e),
                             calopsitas=[],
                             total_calopsitas=0,
                             total_usuarios=0)