#
# class Person:
#     name = 'default'
#     lastname = 'default'
#     age = '18'
#     prof = 'IT'
#     def _set(self, name,lastname):
#         self.name = name
#         self.lastname = lastname
        # self.age = age
        # self.prof = prof

# class Blank(Person):
#     fak = 'default'
#     money = 35000
#
#     def abc(self,fak,money):
#         self.fak = fak
#         self.money = money
#
# student = Person()
# student._set(name=input('Enter the your name:'),lastname=input('Enter the your lastname:'))
# student.abc(fak=input('Your fak:'),money=int(input('Your money:')))
# print(student.name,student.lastname,student.fak,student.money)
# if student.money>=35000:
#     print('Вы не проходите!')
# else:
#     print('Вы зачислены!')
#class Student(Person):
#    vak = 'Fit'
#    cource = 1
#    money = 0
#    def abc(self, vak, cource,money):
#        self.vak = vak
#       # self.cource = cource
#        self.money = money
#
#    def univer(self,):
#alex = Student()
#alex.set('Алекс',21,'proger')
#alex.abc('IR',3,100)
##alex.vak = 'Manas'
#alex.cource = 4
#alex.money = 2000
#print('Меня зовут',alex.name,'Мне',alex.age,'Я работаю',alex.prof,'Учиться в',alex.vak,'На',alex.cource,'курсе','У него', alex.money,'сомов')
#aito = Person()
#aito.set('Aito',18,'Python developer')
#print(aito.name,aito.age,aito.prof)
#taalai = Person()
#taalai.name = 'Taalai'
#taalai.age = 23
##taalai.prof = 'Python developer'
#print('Меня зовут' , taalai.name, 'Мне', taalai.age, 'Я работаю', taalai.prof)

#turat = Person()
#turat.name = 'Turat'
#turat.age = 30
#turat.prof = 'Python junior developer'
#print('Меня зовут', turat.name,'Мне', turat.age, 'Я работаю',turat.prof)#

#kirill = Person()
#kirill.name = 'Kirill'
#kirill.age = 28
#kirill.prof = 'Python senior developer'
#print('Меня зовут', kirill.name,'Мне', kirill.age, 'Я работаю',kirill.prof)

#umut = Person()
#umut.name = 'Turat'
#umut.age = 29
#umut.prof = 'Python middle developer'
#print('Меня зовут', umut.name,'Мне', umut.age, 'Я работаю',umut.prof)#

#aito = Person()
#aito.name = 'Aito'
#aito.age = 18
#aito.prof = 'Python fullstack'
#print('Меня зовут', aito.name,'Мне', aito.age, 'Я работаю',aito.prof)

# class Person:
#   name = 'default'
#   lastname = 'default'
#   age = '18'
#   prof = 'IT'
#
#   def _set(self, name, lastname):
#     self.name = name
#     self.lastname = lastname
#     # self.age = age
#     # self.prof = prof
#
#
#
# class Blank(Person):
#   fak = 'default'
#   __money = 35000
#
#   def __abc(self, fak, money):
#     self.fak = fak
#     self.money = money
#
#
# student = Blank()
#
# student._set(name = input('Введите Ваше имя: '), lastname = input('Введите Вашу фамилию: '))
# student._Blank__abc(fak = input('Ваш факультет: '), money = int(input('Сумма: ')))
# print(student.name, student.lastname, student.fak , student.money )
#
# if student.money >= 35000:
#   print('Вы проходите!')
# else:
#   print('Вы не зачислены!')
# print('1'+'1')

#2 class Car:
#     make = 'Germany'
#     model = 'cla'
#     year = 2017
#     petrol = 70
#     def drive(self, make, model, year, petrol):
#         self.make = input('country:')
#         self.model = input('model:')
#         self.year = int(input('date:'))
#         self.petrol = int(input('petrol:'))
# car = Car()
# car.drive(1,2,3,4)
# print('страна:', car.make, '\nмарка:', car.model, '\nгод выпуска:', car.year, '\nбензин в баке:', car.petrol)
# class Add(Car):
#     odometer = 0
#     def __dictance(self, odometer):
#         self.odometer = car.petrol*10
# abc = Add()
# abc._Add__dictance(1)
# print('на', abc.odometer,' км хватает бензина')
# class Subtract(Car):
#     petrol = 0
#     def __fuel(self, petrol):
#         self.petrol = petrol
# AU = Subtract()
# AU._Subtract__fuel(int(Car.petrol - int(input('dictance:'))*10))
# print('осталось', AU.petrol, 'литр бензина')
# if  AU.petrol > 0:
#     print('Let’s drive!')
# else:
#     print('недостачно бензина!')
class Point3D:
  pass
class Point:
  "Класс для представления для координат точек"
  x = 1
  y = 1


pt = Point()
print(isinstance(pt,Point))
#pt.x = 5
#pt.y = 10
#print(getattr(pt,'x'))
#print(getattr(pt,'z',False))
#print(hasattr(pt,'y'))
#setattr(pt,'z',7)
#print(pt.__dict__)
#delattr(pt,'z')
#print(pt.__dict__)
#setattr(Point,'z',7)

#Point.z = 100
#pt.msg = 'hello'
#res.getattr(pt,'sss',False)
#del pt.x
#print(pt.__dict__)
#print(pt.x,Point.x)
#Point.x = 100
#print(pt.x,pt.y)
#print(id(pt),id(Point),sep='\n')