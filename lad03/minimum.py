a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print(f"Минимум: {minimum}")
