# coding=utf-8
import api_rest

import json
import os
import re
import unittest


class WeatherTestCase(unittest.TestCase):
    """
    WeatherTestCase test case for weather API
    """
    def setUp(self):
        """
        Initialize the test flask server
        """
        api_rest.app.config['TESTING'] = True
        self.app = api_rest.app.test_client()

    def test_weather_city(self):
        """
        Testing if the server send the correct stages and the data has the
        correct format
        """
        stages = ['day', 'min', 'max', 'night', 'eve', 'morn']
        response = self.app.get('/api/madrid')
        data = json.loads(response.data.decode('utf-8'))

        assert stages.sort() == list(data.keys()).sort()
        assert all(re.findall('^\d+(?:\.\d*)?$', str(degrees))
                   for degrees in data.values())


if __name__ == '__main__':
    unittest.main()
