from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import math

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


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

class CalculPrice(Resource):
    def get(self, distance):
        total = distance*0.5
        return {'price': total}


api.add_resource(CalculDistance, '/calculdistance/<float:latitudeA>/<float:longitudeA>/<float:latitudeB>/<float:longitudeB>')
api.add_resource(CalculPrice, '/calculprice/<float:distance>')

if __name__ == '__main__':
    app.run(debug=True)