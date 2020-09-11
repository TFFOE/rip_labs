from math import sqrt
from sys import argv

# Чтение целого числа
def readIntValue():
    successful_input = False
    while (not successful_input):
        try:
            result = int(input("Введите число: "))
            successful_input = True
        except:
            print("Ошибка ввода. Пожалуйста, введите число.")
    return result

# Информационное сообщение
print("Васильев Д. А. Группа: ИУ5-52б.")

# Считывание коэффициентов
if (len(argv) < 2):
    a, b, c = readIntValue(), readIntValue(), readIntValue()

elif (len(argv) == 4):
    try:
        a, b, c = int(argv[1]), int(argv[2]), int(argv[3])
    except:
        print("Неверно введены аргументы.")
        exit(1)

else:
    print("Неверное число аргументов.")
    exit(2)

print ("Вы ввели: {}x^2 + {}x + {} = 0".format(a,b,c))

# Решение уравнения
d = b**2 - 4*a*c

try:
    if (d > 0):
        x1 = (-b - sqrt(d)) / 2 / a
        x2 = (-b + sqrt(d)) / 2 / a
        res = "Получены два корня: x1 = {}, x2 = {}".format(x1, x2)
    elif (d == 0):
        x = -b / 2 / a
        res = "Получен один корень: x = {}".format(x)
    else:
        res = "Уравнение не имеет корней."
except:
    res = "Ошибка при вычислении корней уравнения."

print (res)
