from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://mongo-parser:27017/parser'
app.config['MONGO_HOST'] = 'mongo-parser'
app.config['MONGO_DBNAME'] = 'parser'

mongo = PyMongo(app)


@app.shell_context_processor
def shell_context():
    return {'mongo': mongo}


@app.route('/check', methods=['GET'])
def check():
    return jsonify({'result': 'ok'})
