from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable
from flask_cors import CORS
import math

app = Flask(__name__)
spyne = Spyne(app)
CORS(app)

class SomeSoapService(spyne.Service):
    __service_url_path__ = '/soap/someservice'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
    def distance(self, longitudeA, latitudeA, longitudeB, latitudeB):
        longitudeA=math.radians(longitudeA)
        latitudeA=math.radians(latitudeA)
        longitudeB=math.radians(longitudeB)
        latitudeB=math.radians(latitudeB)
        dlongitude=longitudeB-longitudeA
        radian = math.acos(math.sin(latitudeA)*math.sin(latitudeB)+math.cos(latitudeA)*math.cos(latitudeB)*math.cos(dlongitude))
        result = radian*6378137
        return result

if __name__ == '__main__':
    app.run(host = '0.0.0.0')