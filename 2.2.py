mest = int(input("Введите номер места: "))
if mest % 2 == 0 and mest <= 36:
    print("Верхняя полка купе")
elif mest % 2 != 0 and mest <= 36:
    print("Нижняя полка купе")
elif mest % 2 == 0 and 36 < mest < 55:
    print("Боковая верхняя полка")
elif mest % 2 != 0 and 36 < mest < 55:
    print("Боковая нижняя полка")
elif mest > 54:
    print("Такого места нет")