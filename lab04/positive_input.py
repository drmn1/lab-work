rejected = 0
value = int(input("Введите положительное число: "))

while value <= 0:
    rejected += 1
    value = int(input("Введите положительное число: "))

print(f"Квадрат: {value ** 2}")
print(f"Отклонено попыток: {rejected}")
