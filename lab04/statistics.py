n = int(input("Сколько чисел: "))

total = 0
positives = 0

for i in range(n):
    value = int(input(f"Число {i + 1}: "))
    total += value
    if value > 0:
        positives += 1
    if i == 0:
        maximum = value   # инициализация первым введённым числом
    elif value > maximum:
        maximum = value

print(f"Сумма: {total}")
print(f"Положительных: {positives}")
print(f"Максимум: {maximum}")
