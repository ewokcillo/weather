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


def request_weather(city):
    degrees = get('{0}{1}'.format(ENDPOINT, city))
    return degrees.json()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the Weather forecast")
    parser.add_argument('--city', type=str, required=True,
                        help='Name of the city to get the weather')
    args = parser.parse_args()
    city = vars(args)['city']
    degrees = request_weather(city)
    print('{0}{1}'.format(MESSAGE1, city))
    print('{0}{1}'.format(MESSAGE2, degrees))
