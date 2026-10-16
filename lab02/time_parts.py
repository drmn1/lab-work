total_seconds = int(input("Введите общее количество секунд: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours} ч {minutes} мин {seconds} с")
