import numpy as np

def game_core_v3(number): # Используем метод деление интервала пополам

    count = 0  # счетчик попыток
    #     # number = np.random.randint(1, 101)
    n1 = 1
    n2 = 101

    while True:  #  цикл сжатие интервала
       count += 1
       if number == n1:break
       elif number < (n2 - n1) // 2 + n1:
           n2 = (n2 - n1) // 2 + n1           # сжимаем интервал сверху
       else:
           n1 += (n2 - n1) // 2               # сжимаем интервал снизу
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
      count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

count = 1  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")
for count in range(1, 101):  # более компактный вариант счетчика
    if number == count: break  # выход из цикла, если угадали
count = score_game(game_core_v3)
print(f"Вы угадали число {number} за {count} попыток.")





