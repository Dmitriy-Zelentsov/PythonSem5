# Напишите программу, удаляющую из текста все слова, содержащие "абв".
list = input('Введите текс через пробел:\n')
print(f'Исходный текст: {list}')
n = 'абв'
list = [i for i in list.split() if n not in i]
print(f'Результирующий текс: {" ".join(list)}')
