
import os
from dotenv import load_dotenv
import requests

load_dotenv()


def fetch_weather(api_key, location):
    base_url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': api_key,
        'q': location,
        'api': 'yes'
    }

    try:
        response = requests.get(base_url, params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error: {http_err}')


def display_info(weather_data: dict):
    location = weather_data['location']['name']
    region = weather_data['location']['region']
    country = weather_data['location']['country']
    temp_c = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    wind = weather_data['current']['wind_kph']
    humidity = weather_data['current']['humidity']
    icon = weather_data['current']['condition']['icon']

    print(f'Current weather in {location}, {region}, {country}:')
    print(f'Temperature: {temp_c}')
    print(f'Condition: {condition}')
    print(f'Wind: {wind}')
    print(f'Humidity: {humidity}')
    print(icon)


def safe_data(data: dict, file_name):
    with open(file_name, 'w') as f:
        f.write('Weather data:\n')
        f.write(
            f"Location: {data['location']['name']}, {data['location']['region']}, {data['location']['country']}\n"
        )
        f.write(f'Temperature: {data['current']['temp_c']}\n')
        f.write(f'Condition: {data['current']['condition']['text']}\n')
        f.write(f'Wind: {data['current']['wind_kph']}\n')
        f.write(f'Humidity: {data['current']['humidity']}\n')
        f.write(f'http:{data['current']['condition']['icon']}\n')


def main():
    api_key = os.environ.get('API_KEY')
    data = fetch_weather(api_key, 'Plovdiv')
    print(data)
    display_info(data)
    safe_data(data, './weather.txt')


main()

