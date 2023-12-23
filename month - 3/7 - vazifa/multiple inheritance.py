# bu otasini ham onasini ham bolasi oldi vorislikka !
class Otasi:
    rangi = 'qora'

    def aqilli(self):
        print('Juddayam aqilli')


class Onasi:
    rangi1 = 'oq'

    def pazanda(self):
        print('Qoli juddayam shirin')


class Bolasi(Onasi, Otasi):
    pass


b = Bolasi()

print(b.rangi)
print(b.rangi1)
b.aqilli()
b.pazanda()