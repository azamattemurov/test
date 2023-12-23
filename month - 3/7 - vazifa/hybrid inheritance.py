
class Animal:
    def ovoz(self):
        print('Ovoz chiqara oladi !')


class Animal1(Animal):
    def yurish(self):
        print('Yura oladi !')


class Animal2:
    def uxlash(self):
        print('Uxlay oladi !')


class Mushuk(Animal2, Animal1):
    pass


m = Mushuk()
a = Animal()
a1 = Animal1()
a2 = Animal2()

# Mushuk voris oldi
m.ovoz()
m.yurish()
m.uxlash()
print()
# Animal1 = Animaldan voris oldi !
a1.ovoz()
a1.yurish()
print()
# Animal2 voris olmadi !
a2.uxlash()
print()
# Animal ham voris olmadi !
a.ovoz()
