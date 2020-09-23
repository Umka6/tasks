# def function():
#    print("Hello Umka")
#    print("Hello Dayana")
# function()
# function()
# function()
# print("Hello from outside")
# def function2(x):
#     return 2*x
# a = function2(5)
# function2
# print(a)
# function2(5)
#     print((4355))
# #     d = function2()
# def sum_of_two_numbers(x,y):
#     return x + y
# e = sum_of_two_numbers(6,8)
# print(e)
# def function6(dayanartist):
#      print(dayanartist)
#      print('Hi')
# function6
# def function4():
#     return 9
# print(function4())
# a = function6(16676)
# print(a)
# def function8(x):
#     print(x)
#     print('Hi Umka!')
#     print(3**x)
# a = function8(5)
# print(a)
name1 = 'Nadya'
height1 = 1.78
weight1 = 56
name2 = 'Masha'
height2 = 1.59
weight2 = 45
name3 = 'Kuzya'
height3 = 1.78
weight3 = 89
# def bmi_calculator(name,height,weight):
#     bmi = weight/height**2
#     print('Индекс массы тела' + str(bmi))
#     if bmi<25:
#         return name + " Не имеет лишнего веса"
#     else:
#         return name + " Имеет лишний вес"
# bmi1 = bmi_calculator(name1,height1,weight1)
# bmi3 = bmi_calculator(name3,height3,weight3)
# print(bmi1)
# print(bmi2)
# print(bmi3)
# a = [6,4,0,56,453]
# print(a)
# a.append(46)
# print(a)
# a.append("Hi Umka! How are you?")
# print(a)
# a.append([6,46565])
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# print(a[2])
# print(a[-1])
# print(a[-2])
# a[2] = 133
# print(a)
# a.pop(4)
# print(a)
# b = ['Hey', 'I love you','Miss Korea', 'Miss World']
# print(b)
# b[2],b[0] = b[0],b[2]
# print(b)
#a = [54,5657,54546,4554]
#print(a[0])
#print(a[1])
#print(a[2])
#print(a[3])
#for element in a:
#    print(element)
#for num in a:
#    print(num)
#total_sum = 0
#for e in a:
#   total_sum = total_sum +e
#print(total_sum)

# total_sum = 0
# for i in range(1,100):
#     # total_sum = total_sum +i
#     total_sum +=i
# print(total_sum)


# print(list(range(1,100)))
#total_sum = 0
#for i in range(1,100):
#    if i % 3 == 0:
#        total_sum+=i
#print(total_sum)


# marks = [444,4663,5674,45]
# t1 = 20
# t2 = 24
# tjuly = [20,23,26,26,15,34]
# print(tjuly)

# a=[33,44,345,'hello',[454,6,754]]
# b=[]
# print(type(b))
# print(len(a))
# print(len(b))

# print([444,4444,'hi',0]+[43,23,123,'bye'])
#
# a = [[43,455,289],'hi','should','hello']  #создаем спиок, к-й содержит числа, строки,вложенный список
# a = ['umka']+a  #можно вставить элемент перед переменной a
# print(a*6)  #можно элемент a умножить на любое число
# print('hi' in a) #можем с помощью функции in проверить,есть ли элемент в переменной a

# w = [4,3,2,1,0,-76,85,45]
# print(max(w))
# print(min(w))

# print(sum([344,33,8,9634]))
# w = [64,9009,9864,202,7,6]
# print(sorted(w))  #сортирует список по возрастанию
# print(sorted(w,reverse=True)) #переворачивает список, выведет числа по убыванию

# print(sum([8,654,54,'ih'])) #sum,sorted,max,min при использовании функции мы должны быть уверены,что содержит одинаковые типы данных

# print([1,2,3]==[1,2,3])
# print([100,45]>[87,7778,987]) #при сравнении списков берутся первые элементы,если первый элемент больше,то даже,если остальные элементы будут больше,выйдет False
# print([1,2,3]==[1,2,'h']) #эти элементы не равны,так содержится строка
# marks = [3,5,3,4,4,5]
#print(sum(marks)/len(marks)) #находим среднее число,поделив на функцию len

# a = list(map(int,input().split()))
# print(777 in a) С помощью "map" даем понять, что у нас список, "int" преобразует данные типа строка в целые числа, ".split()" разделяет введенные значения по пробелу между ними, ну и с помощью "in" ищем вхождение числа 777 в список.

# print(sum(list(map(int,input().split()))))
# a = list(map(int,input().split()))
# print(min(a),max(a))
# a = list(map(int,input().split()))
# print(sum(a)/len(a))
#a = [4,74,375,84,2]
#print(a[1:4])
#a = [4,74,375,84,2]
#print(a[1:5])
#a = [4,74,375,84,2]
#print(a[1:-1])
#a = [4,74,375,84,2]
#print(a[2:999])
#a = [4,74,375,84,2]
#print(a[2:])
#a = [4,74,375,84,2]
#print(a[:2])
#a = [4,74,375,84,2]
#print(a[::2]) #взялся через один нечетные элементы
#print(a[::-2]) #каждый 2 элемент с конца списка

# b = [1,7,89,75,653,873,9] #мы создали список
# b[3:5] = 66,53  #срезу индекса присвоили новые значения
# print(b) #вывели результат
# b[2:5] = 76,43 #мы указали срез,но ввели элементы,меньше чем указали
# print(b) #список уменьшился# ## (del(b[3])
# del b[3] #мы указали индекс списка,кот-й нужно удалить
# print(b)#после вывели результат

# a = [1,3,3,2] # мы создали список
# print(a)#вывели результат
# d = a #переменной d присволи значение переменной a
# print(d)#вывели результат
# d[1] = 100#по индексу списка присволи значение 100
# print(d)#вывели результат
# print(a)#вывели результат, переменная a тоже поменяла значение
# d = a[:]#если мы хотим, что переменная a не меняла значение,то берем срез переменной а
# d[2] = 87#присваем новое значение по индексу
# print(d)#вывели резул
# print(a)#

# d = [54, 'hello', 100, True, -78, False, 'potato']
# print(d[2])

# a = list(map(int, input().split()))
# a = a[2:5]
# print(a)

# a = list(map(int, input().split()))
# a = a[3:6]
# print(a)

# a=list(map(int, input().split())) # print(a[len(a)-3:])
# a = list(map(int, input().split()))
# a = a[::2]
# print(a)

# a =list(map(int, input().split()))
# print(a[::-1])

# a = [76,99,8,6,6,5,432,99]#создали список
# a.insert(1,7)#указали перед каким элементом вставить и какое значение присваиваем
# print(a)#Выводим результат

# a = [8,87,6874,34,23,134]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# a.sort(reverse=True)
# print(a)

# a = [8,11,'Привет','True',45.5]
# a.reverse()
# print(a)

# a=list(map(int,input().split()))
# print(a.count(999))

# a = input().upper().split()
# print('-'.join(a))
# print(*['-'.join(i) for i in input().upper().split()])
# a=input().split()
# print("\n".join(a))
# a = int(input())
# b = int(input())
# c = a
# if b > a:
#     c = b
# print(c)

# a = int(input())
# if a < 20000:
#     print(a)
# elif a > 20000:
#     print(a/13*100)

# a = int(input())
# if a < 20000:
#     print(a)
# elif a > 20000:
#     print(a/13*10) #надо подумать

# a = input()
# if a == "Python":
#     print("Да")
# else:
#     print("Нет")

# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# elif b > a:
#     print(b)

# number = int(input())
# number = str(number)
# if number == number[::-1]:
#     print('Yes')
# else:
#     print('No')

# a = map(int, input().split())
# print(str(a[::-1])) #неправильное решение, надо подумать

# a,b,c = map(int,input().split())
# if a+b==c:
#     print("Yes")
# elif a+b!= c:
#     print("No")

# s = input()
# t = input()
# if s == t[::-1]:
#     print('True')
# else:
#     print('False')

# a,b,c = map(int,input().split())
# if a + b > c and a + c > b and b + c > a:
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# if a // 1000 == a % 10 and a // 10 % 10 == a // 100 % 10:
#     print('yes')
# else:
#     print('no')

# a = 35
# if a % 5 == 0:
#     if a > 9 and a < 100:
#         print(1)
#         print(2)
#     else:
#         print(3)
#         print(4)
# else:
#     if a % 2 == 0:
#         print(5)
#         print(6)
# print('end')

# a = 105
# if a % 5 == 0:
#     if a > 9 and a < 100:
#         print(1)
#         print(2)
#     else:
# else:
#     if a % 2 == 0:
#         print(5)
#         print(6)
# print('end')

# a = 47
# if a % 5 == 0:
#     if a > 9 and a < 100:
#         print(1)
#         print(2)
#     else:
#         print(3)
#         print(4)
# else:
#     if a % 2 == 0:
#         print(5)
#         print(6)
#     else:
#         print(7)
#         print(8)
# print('end')

# x = int(input())
# y = int(input())
# if x>0:
#     if y>0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y>0:
#         print(2)
#     else:
#         print(3)
# a = int(input())
# b = int(input())
# if a < b:
#     print("<")
#
# elif a > b:
#     print(">")
# else:
#     if a == b:
#         print("=")
# a = int(input())
# b = int(input())
# c = int(input())
# print(max(a,b,c))
# if a > b > c:
#     print(a)
# elif b > a > c: #условие b не работает
#     print(b)
# else:
#     if c > a > b:
#         print(c)

# tort = 1
# h = int(input())
# if h == 2:
#     print(h//2)
# elif h == 1:
#     print(tort)
# elif h % 2 == 0:
#     print(h)
# else:
#     if h % 2 != 0:
#         print(h)
