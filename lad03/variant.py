value = int(input("Уровень ресурса (0–100): "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 14:
    print("Пополнить")
elif value <= 59:
    print("Достаточно")
else:
    print("Большой запас")
