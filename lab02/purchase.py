total = int(input("Общее количество билетов: "))
capacity = int(input("Билетов в одной пачке: "))

full = total // capacity        # полностью заполненных пачек
remainder = total % capacity    # остаток билетов
needed = (total + capacity - 1) // capacity  # минимальное число пачек

print(f"Полных пачек: {full}")
print(f"Остаток билетов: {remainder}")
print(f"Всего пачек нужно: {needed}")
