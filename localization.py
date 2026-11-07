from unicodedata import name


WEATHER_CONDITIONS = {
    'clear': 'clear',
    'cloudy': 'cloudy',
    'Rain': 'Rain',
    'Drizzle': 'Light Rain',
    'Thunderstorm': 'Thunderstorm',
    'Snow': 'Snow',
    'Mist': 'Mist',
    'Fog': 'Dense fog',
    'Haze': 'Haze',
    'Smoke': 'Smoke',
    'Dust': 'Dust',
    'Sand': 'Sandstorm',
    'Ash': 'Ash',
    'Squall': 'Squall',
    'Tornado': 'Tornado',
}


WIND_DIRECTIONS = [
    'North',
    'North-East',
    'East',
    'South-East',
    'South',
    'South-West',
    'West',
    'North-West'
]


CITIES = {
    "Dhaka": "Dhaka",
    "Khulna": "Khulna",
    "Chittagong": "Chittagong",
    "Chattogram": "Chattogram",
    "Rajshahi": "Rajshahi",
    "Sylhet": "Sylhet",
    "Barisal": "Barisal",
    "Rangpur": "Rangpur",
    "Mymensingh": "Mymensingh",
    "Comilla": "Comilla",
    "Cox's Bazar": "Cox's Bazar",
}


def normalize_number(value):
    """Convert a number or text into a standard string"""
    return str(value)


def get_weather_condition(condition):
    """Return the English description of a weather condition"""
    return WEATHER_CONDITIONS.get(condition, condition)


def get_wind_direction(degree):
    """Convert wind direction degree into a compass direction"""
    if degree is None:
        return 'Unknown'

    index = round(degree / 45) % 8
    return WIND_DIRECTIONS[index]


def get_city_name(name):
    """Return the standardized English city name."""

    if not isinstance(name, str):
        raise TypeError("City name must be a string.")

    city = name.strip().title()

    return CITIES.get(city, city)


def get_display_name(name):
    """Return the city name for display"""
    return get_city_name(name)
