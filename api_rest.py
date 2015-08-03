# coding=utf-8
from flask import Flask
from requests import get

import json

from settings import *


app = Flask(__name__)


@app.route('/api/<city>', methods=['GET'])
def get_weather(city):
    response = get(WEATHER_DATA.format(city))
    json_data = response.json()

    try:
        return_data = json_data['list'][-1]['temp']['eve']
    except:
        return_data = ["Error parsing weather data"]


    return json.dumps(return_data)


if __name__ == '__main__':
    app.debug = True
    app.run(IP_HOST, PORT_HOST)
