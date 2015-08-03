# coding=utf-8
from flask import Flask

import json

from settings import *


app = Flask(__name__)


@app.route('/api/<resource>', methods=['GET'])
def get_weather(resource):
    json_data = []

    return json.dumps(json_data)


if __name__ == '__main__':
    app.debug = True
    app.run(IP_HOST, PORT_HOST)
