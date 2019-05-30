from flask import Flask
from connect_mongo import alunos_collection

app = Flask(__name__)

@app.route("/")
def hello():
    aluno = alunos_collection.find_one()
    return "Nome: "+aluno["nome"]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
