STUDENT_PAYMENT = 6000
GRADUATE_PAYMENT = 8000
class Student():
    def __init__(self, name:str, age:int, groupnum:int, avrrating:int) -> None:
        self.name = name
        self.age = age
        self.groupnum = groupnum
        self.avrrating = avrrating
        self.payment = 0

    def payment_calc(self, init_value) -> None:
        if(self.avrrating == 5): self.payment = init_value
        elif(self.avrrating == 4): self.payment = init_value - 2000
        else: self.payment = 0
        

    def show_info (self)-> None:
        print('ФИО: ' + str(self.name) + '\nВозраст: ' + str(self.age))

    def shows_payment (self) -> None:
        print('Размер стипендии: ' + str(self.payment))
    
    def payment_compare(self, obj)-> None:
        if(self.payment == obj.payment): print('Стипендии одинаковые')
        elif(self.payment < obj.payment): print('Первая стипендия меньше второй')
        elif(self.payment > obj.payment): print('Первая стипендия больше второй')
        else: print('Не сравнимо')

class Graduate(Student):
    def __init__(self, name:str, age:int, groupnum:int, avrrating:int, papername:str) -> None:
        super().__init__(name, age, groupnum, avrrating)
        self.paper = papername


stud1 = Student('Иван Иванович Иванов', 40, 5354208, 5)
stud1.payment_calc(STUDENT_PAYMENT)
stud1.show_info()
stud1.shows_payment()
stud2 = Student('Стив Иванович Иванов', 25, 5354208, 4)
stud2.payment_calc(STUDENT_PAYMENT)
stud1.payment_compare(stud2)
stud3 = Graduate('Стив Иванович Иванов', 25, 5354208, 4, 'Очень умная работа')
stud3.payment_calc(GRADUATE_PAYMENT)
stud2.payment_compare(stud3)