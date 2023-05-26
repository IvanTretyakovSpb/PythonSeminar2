# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет на столе: '))
sum_zero = 0
sum_one = 0
for i in range(1, n+1):
    coin = int(input(f'Введите 0 или 1 для {i}-й монеты: '))
    if coin == 0:
        sum_zero += 1
    else:
        sum_one += 1
if sum_one > sum_zero:
    print(sum_zero)
else:
    print(sum_one)
