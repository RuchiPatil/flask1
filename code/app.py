from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Student(Resource):
    def get(self, name):
        return {'student': name}

api.add_resource(Student, '/student/<string:name>')
#blah


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
    'name' : request_data['name']
    }
    store.append(new_student)
    return jsonify(new_student)

app.run(port=5000)
