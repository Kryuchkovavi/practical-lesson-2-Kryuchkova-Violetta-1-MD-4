a = input("Введите пароль")
b = input("Введите пароль еще раз")
if len(a) == len(b):
    if a.lower() == b.lower():
        if a == b:
            print("Пароль принят")
        else:
            print("Пароль не принят")
    else:
        print("Пароль не принят")
else:
    print("Пароль не принят")