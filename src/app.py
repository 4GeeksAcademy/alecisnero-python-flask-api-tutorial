from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"label": "My first Task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    body = request.get_json()
    request_body = request.json
    todos.append(body)
    print('Incoming request with the following body', request_body)
    return jsonify(todos), 200

@app.route('/todos/<position>', methods=['DELETE'])
def delete_todo(position):
    todos.remove(position)
    print('This is the position to delete', position)
    return 'something'




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=3245, debug = True)