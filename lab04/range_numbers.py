a = int(input("Первое число a: "))
b = int(input("Второе число b: "))

if a < b:
    for number in range(a, b + 1):
        print(number)
elif a > b:
    for number in range(a, b - 1, -1):
        print(number)
else:
    print(a)
