from flask import Flask
app = Flask(__name__)
from flask import jsonify
from flask import request
import json

todos= [
    {'label': 'My first task', 'done': False},
    {'label': 'My second task', 'done': False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    return jsonify(todos)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)