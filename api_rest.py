# coding=utf-8
from flask import Flask
from requests import get

import json

from settings import *


app = Flask(__name__)


@app.route('/api/<city>', methods=['GET'])
def get_weather(city):
    response = get(WEATHER_DATA.format(city))

    if response.status_code == 200:
        json_data = response.json()

        try:
            last_day =  max(json_data['list'], key=lambda x: x['dt'])
            return_data = last_day['temp']
        except:
            return_data = {'error': "Error parsing weather data"}
    else:
        return_data = {'error': "Error obtaining data form openweathermap"}

    return json.dumps(return_data)


if __name__ == '__main__':
    app.debug = True
    app.run(IP_HOST, PORT_HOST)
