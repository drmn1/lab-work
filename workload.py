# Учебная нагрузка по двум предметам
subject1 = input("Название первого предмета: ")
lessons1 = int(input("Количество занятий по первому предмету: "))
duration1 = int(input("Продолжительность одного занятия (мин): "))

subject2 = input("Название второго предмета: ")
lessons2 = int(input("Количество занятий по второму предмету: "))
duration2 = int(input("Продолжительность одного занятия (мин): "))

available_hours = float(input("Доступное время на неделю (часов): "))

time1 = lessons1 * duration1
time2 = lessons2 * duration2
total_minutes = time1 + time2
total_hours = total_minutes / 60
free_hours = available_hours - total_hours
load_4_weeks = total_hours * 4

print()
print(f"{subject1}: {time1} мин")
print(f"{subject2}: {time2} мин")
print(f"Общая нагрузка: {total_minutes} мин ({total_hours:.2f} ч)")
print(f"Свободное время: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {load_4_weeks:.2f} ч")
