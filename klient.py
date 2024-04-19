import requests

from pydantic import BaseModel, Field
from typing import Dict

class Client:
    def __init__(self):
        self.api_key = "55f3a62b-c035-4612-9802-0c55e90a0325"

        self.call = 'http://api.airvisual.com/v2/city?city=Warsaw&state=Mazovia&country=Poland&key='+self.api_key

    def get_data(self):
        print(self.call)
        response = requests.get(self.call)

        if response.status_code == 200:
            try:
                requests.post("http://localhost:5000/data",json=response.json())
            except Exception as e:
                print(f"Error: {e}")



b = Client()
b.get_data()
