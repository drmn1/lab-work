n = int(input("Сколько чисел: "))

count = 0
total = 0

for i in range(n):
    value = int(input(f"Число {i + 1}: "))
    if value != 0:
        count += 1
        total += value

print(f"Количество: {count}")
print(f"Сумма: {total}")
