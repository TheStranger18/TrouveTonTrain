from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import math

app = Flask(__name__)
api = Api(app)

todos = {}


class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class CalculDistance(Resource):
    def get(self, latitudeA, longitudeA, latitudeB, longitudeB):

        latitudeA=math.radians(latitudeA)
        longitudeA=math.radians(longitudeA)
        latitudeB=math.radians(latitudeB)
        longitudeB=math.radians(longitudeB)
        dlongitude=longitudeB-longitudeA
        radian = math.acos(math.sin(latitudeA)*math.sin(latitudeB)+math.cos(latitudeA)*math.cos(latitudeB)*math.cos(dlongitude))
        result = radian*6378137
        result = result/1000
        return {'distance': round(result, 2)}


api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(CalculDistance, '/calculdistance/<float:latitudeA>/<float:longitudeA>/<float:latitudeB>/<float:longitudeB>')

if __name__ == '__main__':
    app.run(debug=True)