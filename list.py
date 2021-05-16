
phones = [3, 5, 7, 9 , 10.5]
print(phones)
phones.append("Python")
print(phones)
print(len(phones))
print(f'Начальный элемент списка: {phones[0]}')
print(f'последний элемент списка: {phones[-1]}')
print(f'элементы списка со второго по четвертый включительно: {phones[1:4]}') 
phones.remove("Python")
print(phones)