from flask import Flask, render_template
from mongoDAO import ConnectionDAO, QuestionDAO

app = Flask(__name__)

from views import *

if __name__ == '__main__':
        
    app.run(debug=False, host='0.0.0.0')
