from flask import render_template
from connect_mongo import questions_collection
from parser_mongo import rank_tags
from main import app

@app.route("/")
def hello():
    rt = rank_tags()
    return render_template('index.html', title='Questions with Python', tags=rt[0:19])