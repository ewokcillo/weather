# coding=utf-8
import logging

"""
Settings to add the global values in the webservice and the command line tool
"""
# WebService settings
IP_HOST='0.0.0.0'
PORT_HOST=5000
DEBUG=True
WEATHER_DATA="http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&units=metric&cnt=2"

#logging
LOG_FILE='api.log'
LOG_LEVEL=logging.DEBUG
