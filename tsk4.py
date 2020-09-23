# num = "I love Java"
# print(num[:6],"Python")

#def decorator(func):
#    def obertka():
#        print('Функция старт')
 #       func()
  #      print('Функция стоп')
       # return obertka()
#def say():
 #   print('Privet')

#def lowercase(func):
#    def wrapper():
#        func_ret = func()
#        change_to_lowercase = func_ret.lower()
#        return change_to_lowercase
#    return wrapper
#def hello_function():
#    return 'HELLO WORLD'

#decorate = lowercase(hello_function)
#print(decorate())

def say(a,b):
    print(a-b)
sayhello = lambda a,b: a+b
say(45,5)
print(sayhello(34,32))
