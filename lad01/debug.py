# Фрагмент А
print("=== Фрагмент А ===")
# Ошибка: строки склеиваются ("23"), нужна сумма чисел (5)
first = "2"
second = "3"
print("До преобразования:", type(first), type(second))
first_num = int(first)
second_num = int(second)
print("После преобразования:", type(first_num), type(second_num))
print("Сумма:", first_num + second_num)  # 5

print()
print("=== Фрагмент Б ===")
# Ошибка: нельзя сложить строку и число (TypeError)
age = input("Возраст: ")  # ввод 17
print("До преобразования:", type(age))
age_num = int(age)
print("После преобразования:", type(age_num))
print("Возраст через год:", age_num + 1)  # 18

print()
print("=== Фрагмент В ===")
# Ошибка: деление имеет приоритет выше сложения
# Было: 4 + 7 + 10 / 3 = 4 + 7 + 3.333... = 14.333...
# Нужно: (4 + 7 + 10) / 3 = 7.0
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Среднее:", average)  # 7.0
