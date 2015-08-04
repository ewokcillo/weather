# weather
weather API and console command

This project get the weather data of a city from openweathermap

# Install
To use this project it's recommended use virtualenvwrapper to install it,
you can install it from this site https://virtualenvwrapper.readthedocs.org

This project is developed in python3.4 and it's no tested in another old versions.

To install the dependencies:
$pip install -r requirements.txt

That's all!!!

# Configuration
You can change some parameters in settings.py file to run the webservice and command line tool

Theese are the values for default.

IP_HOST='0.0.0.0'
PORT_HOST=5000
WEATHER_DATA="http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&units=metric&cnt=2"

# Running
To start the webservice.

$python api_rest.py

And to use the command line tool.

$python weather.py --city=ceuta

or

$python weather.py --city=ceuta --stage=min

# Test
You can check if the project is ok running the tests.

$python weather_test.py

# Doc
In the doc folder you have html documentation generated with pydoc with info about the modules

# Examples
Here you have some examples to test the app.

$ python weather.py --city=ceuta

Weather forecast for tomorrow in ceuta
	Temperature: 26.99
	
$ python weather.py --city=madrid

Weather forecast for tomorrow in madrid
	Temperature: 34.12
	
$ python weather.py --city=malaga

Weather forecast for tomorrow in malaga
	Temperature: 36.37
	
$ python weather.py --city=london

Weather forecast for tomorrow in london
	Temperature: 20.27

$ python weather.py --city=budapest

Weather forecast for tomorrow in budapest
	Temperature: 28.7

$ python weather.py --city=alcantarilla

Weather forecast for tomorrow in alcantarilla
	Temperature: 31.75
