# coding=utf-8
import api_rest

import json
import os
import re
import unittest


class WeatherTestCase(unittest.TestCase):

    def setUp(self):
        api_rest.app.config['TESTING'] = True
        self.app = api_rest.app.test_client()

    def test_weather_city(self):
        stages = ['day', 'min', 'max', 'night', 'eve', 'morn']
        response = self.app.get('/api/madrid')
        data = json.loads(response.data.decode('utf-8'))

        assert stages.sort() == list(data.keys()).sort()
        assert all(re.findall('^\d+(?:\.\d*)?$', str(degrees))
                   for degrees in data.values())


if __name__ == '__main__':
    unittest.main()
