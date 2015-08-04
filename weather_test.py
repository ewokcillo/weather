# coding=utf-8
import api_rest

import os
import re
import unittest


class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        api_rest.app.config['TESTING'] = True
        self.app = api_rest.app.test_client()

    def test_weather_city(self):
        response = self.app.get('/api/madrid')
        degrees = response.data.decode('utf-8')
        assert re.findall('^\d+(?:\.\d*)?$', degrees)

if __name__ == '__main__':
    unittest.main()
