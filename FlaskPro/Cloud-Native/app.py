#!/usr/bin/python3
from flask import Flask, jsonify
import json, sqlite3

app = Flask(__name__)


def list_users():
    conn = sqlite3.connect('mydb.db')
    api_list = []
    cursor = conn.execute('select username,full_name,email,password,id from users')
    for row in cursor:
        a_dict = {}
        a_dict['username'] = row[0]
        a_dict['name'] = row[1]
        a_dict['email'] = row[2]
        a_dict['password'] = row[3]
        a_dict['id'] = row[4]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'user_list': api_list})


@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect('mydb.db')
    api_list = []
    cursor = conn.execute('select bulidtime,version,methods,links from apirelease')
    for row in cursor:
        api = {}
        api['version'] = row[1]
        api['buildtime'] = row[0]
        api['methods'] = row[2]
        api['links'] = row[3]
        api_list.append(api)
    conn.close()
    return jsonify({'api_version': api_list}), 200


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return list_users()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
