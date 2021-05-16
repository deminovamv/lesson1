weather_in_the_city = {
    "city": "Москва",
     "temperature": "20"
}
print(weather_in_the_city['city'])
weather_in_the_city['temperature'] = str(int(weather_in_the_city['temperature']) - 5)
print(weather_in_the_city.get('country'))
print(weather_in_the_city.get('country','Россия'))
print(weather_in_the_city)
weather_in_the_city['date'] ="27.05.2019"
print(f'Длина словаря: {len(weather_in_the_city)}')