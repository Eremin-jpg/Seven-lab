n = int(input("Количество чисел: "))
numbers = [float(input(f"Введите {i+1}-й элемент: ")) for i in range(n)]

minn = numbers.index(min(numbers))

negativeind = []
for i in range(len(numbers)):
    if numbers[i] < 0:
        negativeind.append(i)

if len(negativeind) >= 2:
    first_neg = negativeind[0]
    second_neg = negativeind[1]
    if first_neg < second_neg:
        summ = sum(numbers[first_neg+1 : second_neg])
    else:
        summ = sum(numbers[second_neg+1 : first_neg])
else:
    summ = 0

numbers.sort(key=lambda x: abs(x) > 1)

print("\nРЕЗУЛЬТАТЫ:")
print(f"Индекс минимального элемента: {minn}")
print(f"Сумма элементов между первым и вторым отрицательными элементами: {summ}")
print("Преобразованный список:", numbers)
