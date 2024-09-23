from flask import Flask , request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calopsitas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#cria pagina
#route -> nicolas.legal/
#func o que vai ser exibido
# coloca no ar o site

db = SQLAlchemy(app)

class Calopisita(db.Model):
    __tablename__ = 'calopistas'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    sexo = db.Column(db.String(10), nullable = False)
    idade = db.Column(db.Integer, nullable = False)
    mutacao = db.Column(db.String(100), nullable = False)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/cadastrar-calopisita", methods = ["POST"])
def CadastrarCalopisita():
    nome = request.form['nome']
    sexo = request.form['sexo']
    idade = request.form['idade']
    mutacao = request.form['mutacao']

    novacalopisita = Calopisita(nome=nome,seco=sexo, idade=int(idade),mutacao=mutacao )

    db.session.add(novacalopisita)
    db.session.commit()

    return f"cadastrada com {nome} sucesso"
@app.route("/usuarios/<nicolas>")
def usuarios(nicolas):
    return render_template("usuarios.html", nicolas=nicolas)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)


