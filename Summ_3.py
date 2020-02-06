number = int(input('введите число'))
summ = 0
number_string = number
iteration = number
while iteration > 0:
    summ = summ + number
    iteration = iteration - 1
    number = str(number) + str(number_string)
#   print(number)
    number = int(number)
print(f"сумма будет = {summ}")
