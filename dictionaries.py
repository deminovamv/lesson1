#Создайте словарь:
weather_in_the_city = {
    "city": "Москва",
     "temperature": "20"
}
#Выведите на экран значение ключа city
print(weather_in_the_city['city'])
#Уменьшите значение "temperature" на 5
weather_in_the_city['temperature'] = str(int(weather_in_the_city['temperature']) - 5)
#Задание
#Проверьте, есть ли в словаре ключ country
print(weather_in_the_city.get('country'))
print('country' in weather_in_the_city)
#Выведите значение по-умолчанию "Россия" для ключа country
print(weather_in_the_city.get('country','Россия'))
#Выведите на экран весь словарь
print(weather_in_the_city)
#Добавьте в словарь элемент date со значением "27.05.2019"
weather_in_the_city['date'] ="27.05.2019"
#Выведите на экран длину словаря
print(f'Длина словаря: {len(weather_in_the_city)}')