sec = int(input('Введите число: '))
hours = sec // 3600
hours_res = (hours)
min = (sec % 3600) // 60
min_res = (min)
sec = (sec % 3600) % 60
sec_res = (sec)
if hours > 24:
    print('Количество часов больше, чем в сутках: введите другое число')
else:
    print(f'Время: {hours_res}:{min_res}:{sec_res}')
