# Bu esa ikkta mushuk va kuchuk animal dan vorislik oladi !
class Animal:
    def ovoz(self):
        print('Ovoz chiqara oladi !')
        print('Va juddayam tez yugura oladi !')


class Mushuk(Animal):
    def mushuk(self):
        return 'Mushuk sichqon yeydi'


class Kuchuk(Animal):
    def kuchuk(self):
        return 'Kuchuk non yeydi'

print("Mushuk !")
mushuk = Mushuk()
mushuk.ovoz()
mushuk.mushuk()
print(
)
print("Kuchuk !")
kuchuk = Kuchuk()
kuchuk.ovoz()
kuchuk.kuchuk()
