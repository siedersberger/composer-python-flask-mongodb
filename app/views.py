from flask import render_template, request, redirect, url_for
from connect_mongo import questions_collection
from parser_mongo import rank_tags
from main import app



@app.route("/")
def index():
    return render_template('index.html', title='Questions with ')

@app.route('/consult', methods=['POST'])
def consult():
    selected_language = request.form['language']
    return redirect(url_for('rank', selected_language = selected_language))


@app.route("/rank/<selected_language>")
def rank(selected_language):
    rt = rank_tags(selected_language)
    return render_template('rank.html', title='Questions with ', tags=rt[0:19])