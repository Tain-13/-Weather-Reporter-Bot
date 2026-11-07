import sys
from localization import (
    get_city_name,
    get_weather_condition,
    get_wind_direction,
    normalize_number
)
from logger_setup import get_logger
from weather_client import WeatherClient, WeatherError, parse_weather

sys.stdout.reconfigure(encoding='utf-8')
logger = get_logger('weather_bot', 'weather_bot.log')


def show(info):
    city = get_city_name(info['city'])
    country = info['country']
    place = f'{city},{country}' if country else city
    print(f'\nWeather:{place}')
    print(
        f' Temperature:{normalize_number(info['temp'])}°C '
        f' Feels like {normalize_number(info['feels_like'])}°C '
    )
    print(f'Condition:{get_weather_condition(info['condition'])}')
    print(f'Humidity:{normalize_number(info['humidity'])}%')
    print(
        f'Wind :{normalize_number(info['wind_speed'])} m/s.'
        f'from {get_wind_direction(info['wind_deg'])}\n'
    )


def main():
    client = WeatherClient()
    logger.info('weather bot started')

    while True:
        text = input("Enter city name (press q to quit): ").strip()

        if text.lower() == "q":
            logger.info("Weather bot exited")
            print("Thank you!")
            break

        if not text:
            logger.debug("Empty input")
            print("Please enter a city name.")
            continue

        city = get_city_name(text)
        logger.info('Searching for %s', city)

        try:
            data = client.get_weather(city)
            info = parse_weather(data)
            logger.info(
                'weather for %s : %s c',
                info['city'],
                info['temp']
            )
            show(info)

        except WeatherError as error:
            logger.warning(
                'Search for %s failed : %s',
                city,
                error
            )
            print(error)

        except Exception:
            logger.exception('Unexpected error for %s', city)
            print(
                'An unexcepted error occurred.'
                'check the log file for details'
            )


if __name__ == '__main__':
    main()
