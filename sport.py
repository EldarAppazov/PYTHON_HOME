start_km = int(input('введите количество км с которого вы начнете бегать:'))
finish_km = int(input('введите количество км которого вы хотите достигнуть:'))
day_number = 1
while not (finish_km <= start_km):
    print(day_number, '-й день', "{:.3f}".format(start_km))
    start_km = (start_km * 1.1)
    day_number += 1
print(day_number, '-й день', "{:.3f}".format(start_km))
# не смог добиться чтобы последний день тоже выводился на экран в теле цикла
# пришлось использовать такой костыль
# есть ли в питоне циклы с пост условием?
print(f"на {day_number}-й день вы достигните результата не менее {finish_km} км.")
#не смог