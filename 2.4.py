import random
a = [1,2,3]
if (random.choice(a)) == 1 and (random.choice(a)) == 2:
    print("фиолетовый")
elif (random.choice(a)) == 1 and (random.choice(a)) == 3:
    print("оранжевый")
elif (random.choice(a)) == 2 and (random.choice(a)) == 3:
    print("зеленый")
else:
    print("ОШИБКА (попробуйте еще раз)")