'''
Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых.
И просите ввести заново. Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

'''

number = int(input('Введите целое число, большее 0, но меньшее 10: '))
while not (0 < number < 10):
    number = int(input('Вы ошиблись.\nПовторите ввод: целое число, большее 0, но меньшее 10: '))
print(number, 'в квадрате =', number ** 2)
