from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Dict
from flask.views import View
from typing import List, Optional
from flask import Flask, request, jsonify
from flask.views import MethodView
from datetime import datetime



class Location(BaseModel):
    type: str
    coordinates: List[float]


class Pollution(BaseModel):
    ts: str
    aqius: int
    mainus: str
    aqicn: int
    maincn: str


class Weather(BaseModel):
    ts: str
    tp: int
    pr: int
    hu: int
    ws: float
    wd: int
    ic: str


class Current(BaseModel):
    pollution: Pollution
    weather: Weather


class Data(BaseModel):
    city: str
    state: str
    country: str
    location: Location
    current: Current


class Model(BaseModel):
    status: str
    data: Data

app = Flask(__name__)

class DataView(MethodView):

    def __init__(self):
        self.persystencja={}

    def post(self):
        print("lama")
        print(request.headers)
        data = request.json
        print(data)
        if data is None:
            return jsonify({"error": "Data not provided"}), 400


        result = Model(**data)
        unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds
        self.persystencja[unix_timestamp]=result

        return jsonify(True)

    def get(self,data):
        closest=min(self.persystencja.keys, key=lambda x:abs(x-data))
        return self.persystencja[closest]

app.add_url_rule('/data', view_func=DataView.as_view('data'))

app.add_url_rule('/<int:data>', view_func=DataView.as_view('data'))

if __name__ == '__main__':
    app.run(debug=True)
