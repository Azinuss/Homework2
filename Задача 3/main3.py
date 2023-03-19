import math
class figure ():

    def __init__(self) -> None:
        self.area = 0
        self.perimeter = 0

    def AreaCompare (self, other):
        #if issubclass(type(other), self.__class__): # Невозможно сравнить подклассы?
            if (self.area > other.area): return print('Первая фигура больше второй по площади')
            elif (self.area < other.area): return print('Первая фигура меньше второй по площади')
            elif (self.area == other.area): return print('Первая фигура равна второй по площади')
        #else: return print('Невозможно сравнить')

    def PerimetrCompare (self, other): #не работает если не посчитать периметр заранее
        #if issubclass(other, self.__class__):
            if (self.perimeter > other.perimeter): return print('Первая фигура больше второй по периметру')
            elif (self.perimeter < other.perimeter): return print('Первая фигура меньше второй по периметру')
            elif (self.perimeter == other.perimeter): return print('Первая фигура равна второй по периметру')
        #else: return print('Невозможно сравнить')

    def Area(self):
        return print(f'Площадь фигуры: {self.area}')

    def Perimetr(self):
        return print(f'Периметр фигуры: {self.perimeter}')

class square(figure):
    def __init__(self, x) -> None:
        super().__init__()
        self.a = x
        self.area = self.a**2
        self.perimetr = self.a*4

class rectangle(square):
    def __init__(self, x, y) -> None:
        super().__init__(x)
        self.b = y
        self.area = self.a * self.b
        self.perimetr = (self.a + self.b)*2

class triangle(figure):
    def __init__(self, x,y,z) -> None:
        super().__init__()
        self.a = x
        self.b = y
        self.c = z
        self.perimetr = self.a + self.b + self.c
        __halfprmt = self.perimetr/2
        self.area = math.sqrt(__halfprmt * (__halfprmt - self.a) * (__halfprmt - self.b) * (__halfprmt - self.c)) # формула Герона

class circle(figure):
    def __init__(self, x) -> None:
        super().__init__()
        self.r = x
        self.area = 3.14 * self.r ** 2
        self.perimetr = 2 * 3.14 * self.r

fig1 = square(4)
fig1.Perimetr()
fig1.Area()
fig2 = rectangle(4, 4)
fig1.AreaCompare(fig2)
fig3 = circle(10)
fig4 = triangle(4, 4, 4)
fig3.AreaCompare(fig4)