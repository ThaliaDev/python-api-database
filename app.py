from flask import Flask, request
from flask_restful import Resource, Api
import database
import apsw
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

api = Api(app)

database_name = 'teste.db'
tablename_name = "servidores"

conn = apsw.Connection(database_name)
c = conn.cursor()

class Urls(Resource):
    def post(self):
        data = request.get_json()
        url = data['url']
        sigla = data['sigla']
        database.insert_table(c, data)
        return {'url': url, 'sigla': sigla}, 201

    def get(self):
        c.execute("SELECT id, url, sigla FROM servidores")
        rows = c.fetchall()

        urls = []
        for row in rows:
            urls.append({'id': row[0], 'url': row[1], 'sigla': row[2]})
        return {'urls': urls}

api.add_resource(Urls, '/urls')

if __name__ == '__main__':
    if conn.table_exists(database_name, tablename_name):
        database.create_table(c)
    app.run(debug=True)