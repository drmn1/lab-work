order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

# Первая позиция — карточные игры
item1 = input("Первая позиция: ")
qty1 = int(input(f"Количество «{item1}»: "))
price1 = float(input(f"Цена «{item1}», руб.: "))

# Вторая позиция — головоломки
item2 = input("Вторая позиция: ")
qty2 = int(input(f"Количество «{item2}»: "))
price2 = float(input(f"Цена «{item2}», руб.: "))

delivery = float(input("Стоимость доставки, руб.: "))
paid = float(input("Внесённая сумма, руб.: "))

cost1 = qty1 * price1
cost2 = qty2 * price2
items_cost = cost1 + cost2
total = items_cost + delivery
total_qty = qty1 + qty2
change = paid - total

print("=" * 50)
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer}")
print("-" * 50)
print(f"{item1} | {qty1} | {price1:.2f} | {cost1:.2f}")
print(f"{item2} | {qty2} | {price2:.2f} | {cost2:.2f}")
print("-" * 50)
print(f"Товары без доставки: {items_cost:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итого с доставкой: {total:.2f} руб.")
print(f"Всего единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")
