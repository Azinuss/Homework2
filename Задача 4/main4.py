class student():
    def __init__(self, name:str, age: int, groupnum:int, avrrating:int) -> None:
        self.name = name
        self.age = age
        self.groupnum = groupnum
        self.avrrating = avrrating
        self.paymant = 0
        if(self.avrrating == 5): self.paymant = 6000
        elif(self.avrrating == 4): self.paymant = 4000
        else: self.paymant = 0

    def showinfo (self)-> None:
        print('ФИО: ' + str(self.name) + '\nВозраст: ' + str(self.age))

    def showstipuha (self) -> None:
        print('Размер стипендии: ' + str(self.paymant))
    
    def cmprstipuha(self, obj)-> None:
        if(self.paymant == obj.paymant): print('Стипендии одинаковые')
        elif(self.paymant < obj.paymant): print('Первая стипендия меньше второй')
        elif(self.paymant > obj.paymant): print('Первая стипендия больше второй')
        else: print('Не сравнимо')

class graduate(student):
    def __init__(self, name:str, age:int, groupnum:int, avrrating:int, papername:str) -> None:
        super().__init__(name, age, groupnum, avrrating)
        self.paper = papername
        if(self.avrrating == 5): self.paymant = 8000
        elif(self.avrrating == 4): self.paymant = 6000
        else: self.paymant = 0

stud1 = student('Иван Иванович Иванов', 40, 5354208, 5)
stud1.showinfo()
stud1.showstipuha()
stud2 = student('Стив Иванович Иванов', 25, 5354208, 4)
stud1.cmprstipuha(stud2)
stud3 = graduate('Стив Иванович Иванов', 25, 5354208, 4,'Очень умная работа')
stud2.cmprstipuha(stud3)