# coding=utf-8

from flask import request,make_response
from flask import Flask
import json

app = Flask(__name__)
users_dict = {}

@app.route('/api/users/<int:uid>', methods=['POST'])
def create_user(uid):
    user = request.get_json()
    if uid not in users_dict:
        result = {
          'success': True,
          'msg': 'user created successfully.'
        }
        status_code = 201
        users_dict[uid] = user
    else:
        result = {
          'success': False,
          'msg': 'user already existed.'
        }
        status_code = 500

    response = make_response(json.dumps(result),status_code)
    response.headers["Content-Type"] = 'application/json'
    return response

@app.route('/api/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    user = users_dict.get(uid, {})
    if user:
        user = request.get_json()
        success = True
        status_code = 200
        users_dict[uid] = user
    else:
        success = False
        status_code = 404

    result = {
          'success': success,
          'data': user
        }

    response = make_response(json.dumps(result),status_code)
    response.headers["Content-Type"] = 'application/json'
    return response

@app.route('/api/reset-all')
def clear_user(uid):
    users_dict.clear()
    result = {
          'success': True,
        }

    response = make_response(json.dumps(result))
    response.headers["Content-Type"] = 'application/json'
    return response



if __name__ == '__main__':
    app.run(port=4555, debug=True)