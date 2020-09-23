#def upper(string):
#    return string.upper()
#print(upper('git'))
#def upper(string):
#    return string.upper()

#def lower(string):
#    return string.lower()
#b = ['aito','kirill','taalai','umut','daniar','turat']
#a = ['AITO', 'KIRILL', 'TAALAI', 'UMUT', 'DANIAR', 'TURAT']

#m1 = list(map(upper,b))
#m2 = list(map(lower,a))
#print(m1)
#print(m2)

#def spisok(int):
 #   return int
#a = '256'
#m1 = list(map(spisok,a))
#print(m1)

# def spisok(int):
#         if int == 0:
#             print('Есть 0')
#         else:
#             print('нету')
   # except SyntaxError:
   #     print('Mistake')
        #return int
#a = [2,3,4,5,0]
#m1 = list(map(spisok,a))
#print(m1)

#def spisok(int):
    #if int == 0:
     #   print('Есть 0')
    #else:
     #   print('нету')
    #return int
 #   return int == 0
#a = [2,3,4,5,0]
#b = [3,4,62,2,3]
#m1 = list(map(spisok,a))
#m2 = list(map(spisok,b))
#print(m1)
#print(m2)
#b = ['aito','kirill','taalai','umut','daniar','turat']
#a = list(map(lambda string:string.upper(),b))
#print(a)

#def sum(a,b):
 #   return a + b

#print(sum(10,5))

#a = lambda a, b:a + b
#print(a(5,8))

def poisk(argument):
    return 's' in argument.lower()
def lower(f):
    return f.lower()
g = ['poisk', 'google', 'microsoft', 'spaceX','neirolink','Facebook','WHATSAPP']
a = list(filter(poisk,g))
b = list(map(lower,a))
print(a)

#import

f = list(filter(lambda fit: 's' ))
def poisk(argument):
  return 's' in argument.lower()# Так как мы не знаем будущего списка

def lower(f):
  return f.lower()

g = ['poisk', 'google', 'microsoft', 'spaceX', 'neirolink', 'FACEBOOK', 'WHATSAPP']

a = list(filter(poisk, g))
b = list(map(lower, a))
# print(b)

# c = list(map(lambda string:string.lower(),a))
# print(c)

f = list(filter(lambda a: 's' in a.lower(), g))
print(f)

c = list(map(lambda string:string.lower(),f))
print(c)
def poisk(argument):
  return 's' in argument.lower()# Так как мы не знаем будущего списка

def lower(f):
  return f.lower()

g = ['poisk', 'google', 'microsoft', 'spaceX', 'neirolink', 'FACEBOOK', 'WHATSAPP']

a = list(filter(poisk, g))
b = list(map(lower, a))
# print(b)


