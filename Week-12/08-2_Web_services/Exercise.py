from flask import Flask, jsonify, abort, request
import datetime
import pymysql

app = Flask(__name__)

table = 'names'

def fetch_by_id(name_id, table_name):
    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')
    name = {}
    cursor = cnx.cursor()
    query = ("SELECT name FROM test."+table_name+" WHERE id = %s")
    cursor.execute(query, name_id)
    name = cursor.fetchall()
    cursor.close()
    cnx.close()
    return name

def persist_values_dict(dic, table_name):
    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')
    cursor = cnx.cursor() 
    query = ("INSERT INTO test."+table_name+""
              "(name) "
              "VALUES (%(name)s)")
    cursor.execute(query, dic)
    cnx.commit()
    cursor.close()
    cnx.close() 


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    name = fetch_by_id(task_id, table)
    print(len(name))
    if len(name) == 0:
        abort(404)
    return jsonify({'persons': name[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'name' in request.json:
        abort(400)
    task = {'name': request.json['name']}
    persist_values_dict(task, table)
    return jsonify({'task': task}), 201


if __name__ == '__main__':
    app.run(debug=True)