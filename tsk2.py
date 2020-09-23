# num = int(input ("dtlbnkg jgkfjgkfjg "))
# num2 = int(input ("jgkfjgkfjgkfjg"))
# print(num)

# def arichmetic(a):
#     def res(*args, **kwargs):
#         print("Результат выполнения вашей функции",a(*args,**kwargs))
#
#     return res
#
# @arichmetic
# def operation1(n1,n2):
#     return n1+n2
#
# @arichmetic
# def operation2(n1,n2):
#     return n1-n2
#
# operation1(1,1)
# operation2(1,1)

def house(h):
    def base(*args,**kwargs):
        print(str("base\n" + "floor\n" + "room\n" + "roof\n"))
        h(*args,**kwargs)
    return base
def room(e):
    def r(*args,**kwargs):
        print("First floor")
        r(*args,**kwargs)
    return r
@house
def floor():
    return "Base + floor + room + roof"
floor()