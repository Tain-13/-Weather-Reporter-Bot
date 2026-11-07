import requests

from config import API_KEY
from logger_setup import get_logger

logger = get_logger(__name__, 'weather_bot.log')

URL = 'https://api.openweathermap.org/data/2.5/weather'


class WeatherError(Exception):
    """An error with a user_friendly message."""


class WeatherClient:
    def get_weather(self, city):
        """Fetch weather data for a city and handle API errors."""

        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        logger.info('Requesting weather for %s', city)

        try:
            response = requests.get(
                URL,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            logger.error('Timeout while fetching weather for %s city.')
            raise WeatherClient(
                'The server is not responding, please try again later.'
            )
        except requests.exceptions.ConnectionError:
            logger.error('No internet commection')
            raise WeatherError(
                'No internet connection, please check your network'
            )
        except requests.exceptions.HTTPError as error:
            status = error.response.status_code
            logger.error('HTTP %s error for %s', status, city)
            if status == 404:
                raise WeatherError(
                    'City not found. Please check the spelling'
                )
            if status == 401:
                raise WeatherError(
                    'Invalid API key or API key is not activated'
                )
            if status == 429:
                raise WeatherError(
                    'To many requests. Please wait and try again.'
                )
            raise WeatherError(
                'A server error occurred. Please try again later.'
            )
        except ValueError:
            logger.error('Invalid JSON response for %s', city)
            raise WeatherError(
                'The server returned an unexpected response.'
            )
        except requests.exceptions.RequestException:
            logger.error('Unexcepted request error for %s', city)
            raise WeatherError(
                'Unable to send the weather request.'
            )


def parse_weather(data):
    """Extract and organize weather information from API JSON data."""

    try:
        return {
            "city": data.get("name", "Unknown"),
            "country": data.get("sys", {}).get("country", ""),
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data.get("wind", {}).get("speed", 0),
            "wind_deg": data.get("wind", {}).get("deg"),
            "condition": data["weather"][0]["main"],
        }

    except (KeyError, IndexError, TypeError):
        logger.exception("Failed to parse weather response")
        raise WeatherError(
            "Unable to read the weather information."
        )
