from flask import render_template, request, redirect, url_for
from parser_mongo import ParserTags
from main import app

parser_tags = ParserTags()

@app.route("/")
def index():
    sorted_tags = parser_tags.count_tags()
    return render_template('index.html', title='Consult tags on Stackoverflow platform')

@app.route('/consult', methods=['POST'])
def consult():
    selected_language = request.form['language']
    if selected_language is None or selected_language == "":
        return redirect(url_for('index'))
    return redirect(url_for('rank', selected_language = selected_language))


@app.route("/rank/<selected_language>")
def rank(selected_language):
    rt = parser_tags.rank_tags(selected_language)
    return render_template('rank.html', title='Top tags related with {}'.format(selected_language), selected_tag=selected_language, tags=rt[0:19])