print("Введите кол-во всех чисел.")
kolvo = int(input())
print("Введите ваши числа.")
num = list()
for i in range(kolvo):
    num.append(int(input()))
print("Что вы хотите сделать? \n1. Сложить 2. Умножить 3. Разделить 4. Вычесть")
choice = int(input())
rez = 0
if choice == 1:
    for i in num:
        rez += i
if choice == 2:
    rez += 1
    for i in num:
        rez *= i
if choice == 3:
    rez = num[0]
    num.pop(0)
    for i in num:
        if i != 0:
            rez /= i
        else:
            print("Вы ввели 0, мы его пропустили")
if choice == 4:
    for i in num:
        rez -= i
print("Ответ:", rez)