
def arifmetic (arg1="arg1", arg2="arg2", arg3="arg3"):
    arg1 = int(input())
    arg2 = int(input())
    arg3 = str(input())
    if arg3 == "+":
       return print(arg1.__add__(arg2))
    elif arg3 == "-":
       return print(arg1.__sub__(arg2))
    elif arg3 == "/":
       return print(arg1.__truediv__(arg2))
    elif arg3 == "*":
       return print(arg1.__mul__(arg2))
    else:
        return print("Неизвестная операция")
arifmetic()

