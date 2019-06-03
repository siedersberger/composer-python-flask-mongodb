from flask import Flask, render_template
from connect_mongo import Mongo_connection

app = Flask(__name__)

from views import *

my_db = Mongo_connection(hostname='mongodb')

if __name__ == '__main__':
        
    app.run(debug=False, host='0.0.0.0')
