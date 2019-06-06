import sys
sys.path.append('../')
from flask import Flask, render_template
from libdao.mongoDAO import ConnectionDAO, QuestionDAO

app = Flask(__name__)

from views import *

# connection = ConnectionDAO("localhost")
# questions_controller = QuestionDAO(connection.db)

if __name__ == '__main__':

    app.run(debug=False, host='0.0.0.0')
