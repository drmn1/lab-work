# Вариант 2: Расчет заказа книжного магазина.
order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

item1_name = input("Название первой позиции: ")
item1_qty = int(input("Количество первой позиции: "))
item1_price = float(input("Цена единицы первой позиции: "))

item2_name = input("Название второй позиции: ")
item2_qty = int(input("Количество второй позиции: "))
item2_price = float(input("Цена единицы второй позиции: "))

delivery = float(input("Стоимость доставки: "))
paid = float(input("Внесённая сумма: "))

cost1 = item1_qty * item1_price
cost2 = item2_qty * item2_price
goods_total = cost1 + cost2
total = goods_total + delivery
total_qty = item1_qty + item2_qty
change = paid - total

print()
print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer}")
print(f"{item1_name} | {item1_qty} | {item1_price:.2f} | {cost1:.2f}")
print(f"{item2_name} | {item2_qty} | {item2_price:.2f} | {cost2:.2f}")
print(f"Стоимость товаров: {goods_total:.2f}")
print(f"Доставка: {delivery:.2f}")
print(f"Итого к оплате: {total:.2f}")
print(f"Всего единиц: {total_qty}")
print(f"Сдача: {change:.2f}")
