import os

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('OPENWEATHER_API_KEY')


if not API_KEY:
    raise ValueError('OpenWeather API key is missing.')
