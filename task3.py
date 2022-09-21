import math
from math import acos


def sinus():
    b = int(input("Введите значение:\n"))
    print(math.sin(b))


def cosinus():
    b = int(input("Введите значение:\n"))
    print(math.cos(b))


def tangens():
    b = int(input("Введите значение:\n"))
    print(math.tan(b))


def catangens():
    b = int(input("Введите значение:\n"))
    print(math.cos(b) / math.sin(b))


def arsin():
    b = int(input("Введите значение:\n"))
    print(math.asin(b))


def arccosinus():
    b = int(input("Введите значение:\n"))
    print(acos(b))


def artangens():
    b = int(input("Введите значение:\n"))
    print(math.atan(b))


def pii():
    print(math.pi)


def total():
    b = int(input("Введите первое значение:\n"))
    c = int(input("Введите второе значение:\n"))
    print(b + c)
    input("Нажмите (Enter), чтобы продолжить")


def min():
    b = int(input("Введите первое значение:\n"))
    c = int(input("Введите второе значение:\n"))
    print(b - c)
    input("Нажмите (Enter), чтобы продолжить")


def multiplication():
    b = int(input("Введите первое значение:\n"))
    c = int(input("Введите второе значение:\n"))
    print(b * c)
    input("Нажмите (Enter), чтобы продолжить")


def division():
    while True:
        b = int(input("Введите первое значение:\n"))
        c = int(input("Введите второе значение:\n"))
        if c == 0:
            print("Учитель не говорил, что на ноль делить нельзя?")
            input("Нажмите (Enter), чтобы продолжить")
            continue
        else:
            print(b / c)
            input("Нажмите (Enter), чтобы продолжить")
            break


def exponentiation():
    b = int(input("Введите значение:\n"))
    step = int(input("Введите в какую степень возвести число:\n"))
    print(b ** step)
    input("Нажмите (Enter), чтобы продолжить")


def square():
    b = int(input("Введите значение:\n"))
    print(math.sqrt(b))
    input("Нажмите (Enter), чтобы продолжить")


def cube():
    b = int(input("Введите значение:\n"))
    print(b ** (1 / 3))
    input("Нажмите (Enter), чтобы продолжить")


save = []

while True:
    a = input(
        "Выберети действие +,-,*,/,\nвозвести в степень\nквадратный корень\nкубический корень\nсинус\nкосинус\nтангенс\nкотангенс\n"
        "арксинус\nарккосинус\nарктангенс\n(off = END)\n")
    if a == "+":
        start = total()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "синус":
        start = sinus()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "косинус":
        start = cosinus()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "тангенс":
        start = tangens()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "котангенс":
        start = catangens()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "арксинус":
        start = arsin()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "арккосинус":
        start = arccosinus()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "арктангенс":
        start = artangens()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a == "-":
        start = min()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a == "*":
        start = multiplication()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a == "/":
        start = division()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "возвести в степень":
        start = exponentiation()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "квадратный корень":
        start = square()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "кубический корень":
        start = cube()
        input("Нажмите (Enter), чтобы продолжить")
        continue
    elif a.lower() == "off":
        break
    else:
        print("Введеного вами запроса не существует")
        input("Нажмите (Enter), чтобы продолжить")
        continue
