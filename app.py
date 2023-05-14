from flask import Flask, request
from flask_restful import Resource, Api
import apsw
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)

database_name = 'server.db'
tablename_name = "servidores"

conn = apsw.Connection(database_name)
c = conn.cursor()


class Urls(Resource):
    def post(self):
        data = request.get_json()
        url = data['url']
        sigla = data['sigla']
        c.execute("INSERT INTO servidores (url, sigla) VALUES (?,?)",
                  (data['url'], data['sigla']))
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
        c.execute(
            f"CREATE TABLE {tablename_name} (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, url TEXT NOT NULL, sigla TEXT NOT NULL);")
    app.run(debug=True)
