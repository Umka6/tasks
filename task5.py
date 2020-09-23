#user = input("enter the password")
#password = 'guru'
#count = 1
#while password != user:
#    print('password false',count)
#    count =1
#    user = input('enter the password')
#    if count > 5:
#        break
#        print("Goodbye")
#print('Hi,password true')
user = input("enter the password")
password = 'guru'
count = 1
if user == password:
    print('verno')
while user != password:
    print('ne verno')
    user = input('enter the password:')
    count +=1
    print(count)
    if count > 5:
        break
        print('neverno')
print('verno')

