from flask import Flask, render_template

app = Flask(__name__)

from views import *

# connection = ConnectionDAO("localhost")
# questions_controller = QuestionDAO(connection.db)

if __name__ == '__main__':

    app.run(debug=False, host='0.0.0.0')
