A = []
for i in range(10):
    num = int(input(f"Введите элемент {i+1}: "))
    A.append(num)

proizv = 1
f = False

for i in A:
    if A[i] < 0:
        proizv *= A[i]
        f = True

if f:
    print("Произведение отрицательных элементов:", proizv)
else:
    print("Отрицательные элементы не найдены.")
