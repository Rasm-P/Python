from flask import Flask, jsonify, abort, request
import datetime
import pymysql

#3. Gem dataen i en database med PyMySQL og lav et Webservice api med en GET metode der returnere dataen.
app = Flask(__name__)

table = 'iphones'

def fetch_by_id(table_name):
    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')
    name = {}
    cursor = cnx.cursor()
    query = ("SELECT * FROM test."+table_name)
    cursor.execute(query)
    name = cursor.fetchall()
    cursor.close()
    cnx.close()
    return name

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_task():
    name = fetch_by_id(table)
    print(len(name))
    if len(name) == 0:
        abort(404)
    return jsonify({'Iphones': name})

if __name__ == '__main__':
    app.run(debug=True)