from collections import namedtuple

store = []


def adddd():
    store_add = namedtuple("Товар", "Название цена")
    a = input("Введите название товара\n")
    b = input("Введите цену товара\n")
    final = store_add(a, b)
    store.append(final)
    print("Ваш товар добавлен в магазин")


print("Это ваш магазин, давайте добавим первый товар")

adddd()

while True:
    choose = input("Добавить еще товар(add)\n"
                   "посмотреть все товары в наличие(look)"
                   "\nзавершить программу(off)\n")
    if choose.lower() == "add":
        adddd()
        continue
    elif choose.lower() == "look":
        for i in store:
            print(i)
        input("Enter чтобы продолжить")
        continue
    elif choose.lower() == "off":
        break
    else:
        print("Такой команды нет в нашем списке")
