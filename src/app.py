from flask import Flask;
from flask import Flask, jsonify, request;
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def getTodos():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todo_delete = todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)



#hay que abrir el puerto y ponerle publico para que funcione postman
#pipenv run python src/app.py para ejecutarlo

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)