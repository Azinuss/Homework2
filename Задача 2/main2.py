def fun(fn, mass) -> list:
    return list(filter(fn,mass))

mass = ['Пробелы тут есть', 'А тут первая', 'мало', 'арбуз']
print(mass)
# print(list(filter(lambda x: ' ' not in x, mass)))
print(fun(lambda x: ' ' not in x, mass))
print(fun(lambda x: 'а' not in x[0], map(lambda x: x.lower(), mass)))
print(fun(lambda x:  5 > len(x), mass))