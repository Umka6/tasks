# git = "Python "
# print(git*5)

#s = [4,10]
#print(list(range(1,5)))
#print(list(range(*s))

#def f(a,b,c,d):
#    print(a,b,c,d)
#f(1,2,3,4)
#a = ("hello",True,78,[3,4,5])
#f(*a)

def func(**args):
    return args
print(func(short='dict', longer = 'dictionary')) #оборачивает в словарь