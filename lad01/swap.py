# Обмен значениями двух переменных через третью.
first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print(f"Исходно: {first_room} и {second_room}")

temp = first_room
first_room = second_room
second_room = temp

print(f"После обмена: {first_room} и {second_room}")
