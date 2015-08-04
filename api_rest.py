# coding=utf-8
from flask import Flask
from requests import get

import logging
from logging import FileHandler
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
            app.logger.error(return_data)
    else:
        return_data = {'error': "Error obtaining data form openweathermap"}
        app.logger.error(return_data)

    return json.dumps(return_data)


if __name__ == '__main__':
    file_handler = FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)
    app.logger.addHandler(file_handler)
    app.debug = DEBUG
    app.run(IP_HOST, PORT_HOST)
