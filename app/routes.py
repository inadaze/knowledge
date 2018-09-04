from app import app
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort

#start server with 'flask run'

#curl http://127.0.0.1:5000/api/v1.0/seed/1
@app.route('/api/v1.0/seed/<int:seed_id>', methods=['GET'])
def index(seed_id):
    return jsonify({'seed_id': seed_id}), 201

#curl -i -H "Content-Type: application/json" -X POST -d "{\"content\":\"hello\"}" http://127.0.0.1:5000/api/v1.0/seed/create
@app.route('/api/v1.0/seed/create', methods=['POST'])
def create_seed():
    if not request.json or not 'content' in request.json:
        abort(400)
    return jsonify({'seed_content': request.json['content']}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)