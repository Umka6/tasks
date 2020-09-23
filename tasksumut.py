#a = int(input())
#b = int(input())
#c = int(input())
#print(max((a + b + c), (a + b * c), (a * (b + c)), (a * b * c), (a + b) * c))

#print(1,2,3,sep=',',end='')
#print(3,5,6,sep='???')

# rubles = 10
# kop = 99
# print('У меня есть',rubles,'рублей',kop,'копеек')
# rubles = 10
# kop = 99
# print('У меня есть %s рублей %s копеек'%(rubles,kop))

# a = int(input())
# b = a - 1
# c = a + 1
# print(b,a,c,sep='<')

#x = int(input())
#a = x //10000
#b = x //1000%10
#c = x //100%10
#d = x //10%10
#print(a,d)

#x = int(input())
#print(x//100%10)

# x = int(input())
# a =
# print(a)

# a=int(input("Сколько у вас есть яблок: "))
# b=int(input("Сколько всего вас: "))
# c=a//b
# d=a%b
# print("На каждого будет по",c,"яблок.И у нас остаеться",d,".")

#n = int(input())
#print(n//9%9)

#n = int(input())
#h = n//60%24
#m = n%60
#print(h,m)

#n = int(input())
#n = n+1
#print(n)

#n=int(input())
#print(n+1+(n+1)%2)

#n = int(input())
#h = n//3600%60
#m = n%3600%60
#s = n%60%60
#print(h,m,s,sep=':')

# n = int(input())
#
# x=n//3600%24 #часы
#
# x1n=n//60//10%6 #десятки минут
#
# x1=n//60%10 #минут
#
# x2n=n//10%6 #десятки секунд
#
# x2=n%10 #секунд
#
# print(f'{x}:{x1n}{x1}:{x2n}{x2}')


#a = 33
#print(a>=21 and a<=45)

#a = 517
#print((a>5 or a%2==0) and a%10==7)

# a = int(input())
# print(a>0)

#a = int(input())
#print(a%2 == 0)

#a = int(input())
#print(a%6 == 0)

#a = int(input())
#print(a % 9 != 0)

#b = int(input())
#print(b%10==2)

# a,b = map(int,input().split())
#print(a%7==0 and b%7==0)
#
# a,b,c = map(int,input().split())
# print(a==b and a==c and b==c)


#a = int(input())
#print(a>5 and a<=19)

#a = input()
#b = input()
#c = 'awesome'
#print(a==c or b==c)

#a,b,c = map(int,input().split())
#print(a==b or a == c or b==c)

#a = int(input())
#print(9 < int(a) <= 99)

#a,b,c = map(int,input().split())
#print(a*a+b*b==c*c)

#a,b,c=map(int,input().split())

#gip=max(a,b,c)

#kat1=min(a,b,c)

#kat2=a*b*c/gip/kat1

#print(kat1**2+kat2**2==gip**2)

#import math
#math.trunc(32)

#company = int(input()) #комания людей
#taxi = 0 #такси
#taxi += company // 4 #какое значение примет теперь переменная такси
#if company % 4 > 0: #если остаток от деления больше нуля (А при делении на 4 какие остатки могут быть?)
#      taxi +=1  #то что добавляется в переменную такси и почему
#print(taxi)

#n = int(input())
#print(int(n+9)/10)

#x = 5
#y = 10
#print(y > x * x or y >= 2 * x and x < y)

#a = int(input())
#b = int(input())
#c = int(input())
#desk1 = a //2+a%2
#desk2 = b//2+b%2
#desk3 = c //2+c%2
#print(desk1+desk2+desk3)

# l,m,n = map(int,input().split())
# a = (l+m)*2*n//16
# if a % 4!=0:
#     a+=1
# print(a)

# a = '''Я стану крутым программистом!\n'''
# print(a*3)

# f = input()
# d = input()
# print(f)
# print(d)

# a = input()
# b = input()
# c = input()
# print(c)
# print(b)
# print(a)

# a = input()
# print(a, a, a, a)

# a = input()
# print(len(a))

# a = input()
# b = input()
# print(b+a)

#print(input()*3)

# a = input()
# print(a)
#
# a = input()
# a = a[0]
# print(a)

# print(input()[-1])

#print(input()[:4])

#print(input()[::2])
#print(input()[1::2])
#print(input()[:14])
#print(input()[::-1])
#print(input()[-4:])
#print(input()[-1::-3])

#s = input().upper()
#print(s)

#print(input().lower())

#print(input().count('e'))

#a = input()
#print(a.count('e'))

#a = input()
#print(a.count('e'))

#a = input().lower()
#print(a.replace('w','',-1))

#a = input().lower()
#print(a.replace('w','').replace('z',''))

#a = input().find('a')
#print(a)

#print(input().rfind('a'))

#a = input()
#print(len(a.split()))

#a = input()
#a = ",".join(a.split())
#print(a)

#name = input()
#surname = input()
#print("Здравствуйте, " + surname,name)

#[print(i) for i in [input() for _ in range(3)][::-1]]

#a,b,c = input(),input(),input()
#print(c,b,a,sep= '\n')

#a = int(input())
#for i in range(1,10):
#    print(i,'*')

#print('31', '12', '2019', sep='-')

#print('Mercury', 'Venus', sep='*', end='!')
#print('Mars', 'Jupiter', sep='**', end='?')



#print('a', 'b', 'c', sep='*')
#print('d', 'e', 'f', sep='**', end='')
#print('g', 'h', 'i', sep='+', end='%')
#print('j', 'k', 'l', sep='-', end='\n')
#print('m', 'n', 'o', sep='/', end='!')
#print('p', 'q', 'r', sep='1', end='%')
#print('s', 't', 'u', sep='&', end='\n')
#print('v', 'w', 'x', sep='%')
#print('y', 'z', sep='/', end='!')
# a = input()
# b = input()
# c = input()
# print(a,b,c,sep="***")

#print("I","like","Python",sep="***")


# a = input()
# b = input()
# c = input()
# d = input()
# print(b, c, d, sep= a)
#print('Python', end='+')
#print('C#', end='=')
#print('awesome')

# a = int(input())
# b = int(input())
# h = int(input())
# if h <= a  b:
#     print("Это нормально")
# elif h >= a >= b:
#     print("Пересып")
# elif a <= h <= b:
#     print("Недосып")


a = "hello world"
print(a[:2:4])