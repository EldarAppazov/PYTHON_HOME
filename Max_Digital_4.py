number = int(input('введите чило: '))
max_digital = 0
if number < 0:
    number = abs(number)
while number > 0:
    if max_digital < (number % 10):
        max_digital = number % 10
    number = number // 10
print(f" максимальная цифра в числе = {max_digital}")
