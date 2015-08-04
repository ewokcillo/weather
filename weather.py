# coding=utf-8
from requests import get

import argparse

try:
    from settings import *
except:
    IP_HOST="localhost"
    PORT_HOST=5000


ENDPOINT='http://{0}:{1}/api/'.format(IP_HOST, PORT_HOST)
MESSAGE1="Weather forecast for tomorrow in "
MESSAGE2="\tTemperature: "


def request_weather(city, stage):
    data = get('{0}{1}'.format(ENDPOINT, city))
    degrees = data.json()[stage]
    return degrees


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the Weather forecast")
    parser.add_argument('--city', type=str, required=True,
                        help='Name of the city to get the weather')
    parser.add_argument('--stage', type=str, default='day',
                        choices=['day', 'min', 'max', 'night', 'eve', 'morn'],
                        help='Stage of the day')

    args = vars(parser.parse_args())
    degrees = request_weather(**args)
    print('{0}{1}'.format(MESSAGE1, args['city']))
    print('{0}{1}'.format(MESSAGE2, degrees))
