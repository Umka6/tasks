# a = 1
# b = 0
# print(a/0)

#try:
#    a = 1/0
#except ZeroDivisionError:
#    k = 0
#    print('На ноль делить нельзя')
#print(k)

#try:
#    a = input('Введите первое число:')
#    b = input('Введите второе число:')
    #print('Результат:', int(a) / int(b))
#    result = int(a) / int(b)

#except ValueError:
#    print('Введите только числа')
#except ZeroDivisionError:
#    print('На ноль делить нельзя')
#except NameError:
#    print('Нету переменной для вывода, переменная result')
#else:
 #   print('Результат делителя:', result)
#except Exception:
#    print('У тебя в программе ошибки')
#finally:
#    print('Все данные введены правильно, программа выполнена на 100%')
    #print('Обратитесь в службу поддержки')

#try:
#    a = 'hello'
#    b = input('enter the num:')
#    result = a/b
#except TypeError:
#    print('it is type error')
#else:
#    print('result is',result)

#try:
#    a = [1,4,6,5,7]
#    result=a[8]
#except IndexError:
#    print('Нет в списке')
#else:
#    print('result is',result)

#try:
#    b = 'hello'
#    result=a+b

#except TypeError:
#    print('Erorr')
#else:
#    print('resilt is',result)

#try:
#    d = {'a':1, 'b':2,'c':3}
#    result = d['d']
#except KeyError:
#    print('erorr')

#try:
#    a = int(input('Enter the number:'))
#    result = a ** b
#except NameError:
#    print('Name is not defined')
#else:
#    print('result is', result)

#try:
#    a = int(input('Enter the number:'))
#    b = int(input('Enter the number:'))
#    result = a // b
#except ValueError:
#    print('Enter the number')
#else:
#    print(result)

#try:
#    a = [76,44,3,22,64,36]
#    result = a[7]
#except IndexError:
#    print('list is not defined')
#else:
#    print(result*2)

#try:
#    a = {'a':43,'b':53,'c':84}
#    result = a['e']
#except KeyError:
#    print('Key is not defined')

#def calc(n):

#    return 10 * n / 1000
#print(calc(1000))

#def calc(n):
#    n = int(n)
#    return 10 * n / 1000
#print(calc('1000'))

# def calc(n):
#     try:
#         n = int(n)
#     except:
#         n = 0
#         return 10 * n / 1000
#
# print(calc('hjjk'))

#def calc(n):
#    try:
#        n = int(n)
#    except Exception:
#        print('Something went wrong')
#    else:
#        return 10 * n / 1000

#print(calc('hjjk'))

def calc(n):
    try:
        n = int(n)
    except Exception as e:
        print(e)
        n = 0

        return 10 * n / 1000

print(calc('hjjk'))