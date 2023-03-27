import math
class Figure ():

    def __init__(self) -> None:
        self.area = 0
        self.perimeter = 0

    def area_compare (self, other) -> bool:
        #if issubclass(type(o и функции принято называть в sther), self.__class__): # Невозможно сравнить подклассы?
            if (self.area > other.area): return True
            elif (self.area < other.area): return False
            elif (self.area == other.area): return False
        #else: return print('Невозможно сравнить')

    def perimeter_compare (self, other): #не работает если не посчитать периметр заранее
        #if issubclass(other, self.__class__):
            if (self.perimeter > other.perimeter): return True
            elif (self.perimeter < other.perimeter): return False
            elif (self.perimeter == other.perimeter): return False
        #else: return print('Невозможно сравнить')

    def area_of(self) -> float:
        return self.area

    def perimeter_of(self) -> float:
        return self.perimeter

class Square(Figure):
    def __init__(self, a:int) -> None:
        super().__init__()
        self.a = a
        self.area = self.a**2
        self.perimeter = self.a*4

class Rectangle(Square):
    def __init__(self, a:int, b:int) -> None:
        super().__init__(a)
        self.b = b
        self.area = self.a * self.b
        self.perimeter = (self.a + self.b)*2

class Triangle(Figure):
    def __init__(self, a:int, b:int, c:int) -> None:
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.perimeter = self.a + self.b + self.c
        __halfprmt = self.perimeter/2
        self.area = math.sqrt(__halfprmt * (__halfprmt - self.a) * (__halfprmt - self.b) * (__halfprmt - self.c)) # формула Герона

class Circle(Figure):
    def __init__(self, x) -> None:
        super().__init__()
        self.r = x
        self.area = 3.14 * self.r ** 2
        self.perimeter = 2 * 3.14 * self.r

fig1 = Square(4)
print(f'Периметр фигуры: {fig1.perimeter_of()}')
print(f'Площадь фигуры: {fig1.area_of()}')
fig2 = Rectangle(4, 4)
print(fig1.area_compare(fig2))
fig3 = Circle(10)
fig4 = Triangle(4, 4, 4)
print(fig3.area_compare(fig4))