from flask import Flask, flash, redirect, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Adicione uma chave secreta para o flash
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calopsitas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Calopisita(db.Model):
    __tablename__ = 'calopistas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    mutacao = db.Column(db.String(100), nullable=False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar-calopisita", methods=["POST"])
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

@app.route("/usuarios/<nicolas>")
def usuarios(nicolas):
    return render_template("usuarios.html", nicolas=nicolas)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
