from flask import render_template
from connect_mongo import alunos_collection
from main import app

@app.route("/")
def hello():
    aluno = alunos_collection.find({})
    return render_template('index.html', title='Songs list', alunos=aluno)