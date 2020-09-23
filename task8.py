# p = open('text.txt','r')
# a = p.read()
# print(a)
# p.close()



# p = open('text.txt','r')
# a = p.readlines()
# print(a)
# p.close()



#with open('text.txt','r') as a:
#    for line in a:
#        print(line)

#with open('text.txt', 'r+') as f:
#    a = f.read().split()
#    print(max(a,key=len))         #считает самую длинную строку

#with open('text.txt') as f:
#    print(sorted(f.read().split('\n'),key = len)[::-1]) #сортирует и выводит список,разделенные через пробел

#s = ['gg','ggwp','bg','glhf']
#s = [i + '\n' for i in s]
#with open('text.txt','w') as f:  #выводит список с каждой новой строки
#    f.writelines(s)

#with open('text.txt','r+') as a:
#    print(len(a.readlines()))    #считает длину строки

#aito = open('text.txt','w')
#print('Имя файла:', aito.name)
#print('Файл закрыт:',aito.closed)
#print('В каком режиме файл открыт:',aito.mode) #проверяет файл открыт или закрыт

#a = open('text.txt','rw')
#for line in a:
#    print(a)
#a.close()

#file = open('text.txt', encoding='utf-8')
#print(file.read())  #открываем текст, используем функию, которая работает с кириллицей

#file = open(r'/home/umut/Documents/text.txt')
#print(file.read()) #открываем текст,скопировали путь файла Absolute Path,будет тот же результат

#file = open('text.txt',encoding='utf-8')
#print(file.read(3))
#print(file.read(3))
#file.seek(0)
#print(file.read(3))

#file = open('text.txt',encoding='utf-8')
#print(file.readline())
#print(file.readline())  #берет целую строку

#file = open('text.txt',encoding='utf-8')
#for row in file:  #можно циклом пройтись по файлу и вывести весь текст
#    print(row)

#file = open('text.txt',encoding='utf-8')
#for row in file:  #можно циклом пройтись по файлу и вывести весь текст
#    for letter in row:
#        print(letter)

#file = open('text.txt',encoding='utf-8')
#s = file.readlines()   #строку превращает спикок,каждая строка заканчивается служебным символо '\n' переноса строки
#print(s)

#file = open('text.txt','w')
#file.write('hello')    #выводит текст, запись файла
#print(file)

#file = open('text.txt','w')
#file.write('hello') #выводит строки вместе
#file.write('hello')
#file.write('hello')

#file = open('text.txt','w')
#file.write('hello\n')  #переносит текст на новую строку
#file.write('hello\n')
#file.write('hello\n')

#file = open('text.txt','a')
#file.write('hi\n') #добавляет в конец файла

#file = open('redme.txt','w')
#print(file)
#type(file)

#with open('text.txt') as f:
#    a = f.read().split()
#    print(max(a, key=len))

#with open('text.txt') as f:
#    print(sorted(f.read().split('\n'),key = len)[::-1])

text = 'out_text'
f = open('umka.txt','w')
f.write(text)
f.closed