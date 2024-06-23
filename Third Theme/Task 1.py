total = 0
count = 0

while True:
    number = float(input("Введите число (или 0 для завершения): "))
    if number == 0:
        break
    total += number
    count += 1

if count == 0:
    print("Среднее значение: 0")
else:
    print("Среднее значение:", total / count)
