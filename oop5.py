#class Cat:
#    breed = 'siams'

    # def set_value(self, name, age=0):
    #     self.name = name
    #     self.age = age

#bob = Cat()
#bob.set_value('Bob')
#print(bob.name,bob.age)

#    def __init__(self,name,breed='brid',age=1,color='white'):
#        self.name = name
#        self.age = age
#        self.breed = breed
#        self.color = color
# walt = Cat('Walt')
# walt.Cat()
# #print(str(walt))
#
# #debug this after
# class Dog:
#     name = 'Wolt'
#     age = 12
#
#     def doggy(self,name,age):
#         self.name = name
#         self.age = age
#
# wo.Dog()
# wo.doggy('Wolt',4)
# print(wo.name,wo.age)

class Cat:
    breed = 'brid'
    def set_value(self, name, age=0):
        self.name = name
        self.age = age
    def __init__(self,name, breed='brid', age=1, color='white'):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

#bob = Cat()
#bob.set_value('Bob')
#print(bob.name,bob.age)
walt = Cat('Walt','siams',4,'black')
bobi = Cat('Bob','grid',3,'pink')
print(walt.name, walt.age,walt.breed,walt.color)
print(bobi.name, bobi.age,bobi.breed,bobi.color)