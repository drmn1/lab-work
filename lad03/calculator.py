a = float(input("Первое число: "))
b = float(input("Второе число: "))
op = input("Операция (+, -, *, /): ")

if op == "+":
    print(f"{a + b:.2f}")
elif op == "-":
    print(f"{a - b:.2f}")
elif op == "*":
    print(f"{a * b:.2f}")
elif op == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"{a / b:.2f}")
else:
    print("Неизвестная операция")
