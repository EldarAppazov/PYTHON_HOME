time_in_seconds = int(input('введите количество секунд: '))
hour = time_in_seconds // 3600
balance = time_in_seconds % 3600
minutes = balance // 60
balance = balance % 60
print(f"{time_in_seconds} секунд будет состовлять \nhh:mm:ss {hour}:{minutes}:{balance}")

