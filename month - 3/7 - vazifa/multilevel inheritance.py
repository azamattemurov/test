# ketma ket otasini onasi vorislikka oldi onasini esa bolasi !
class Otasi:
    rangi = 'qora'

    def aqilli(self):
        print('Juddayam aqilli')


class Onasi(Otasi):
    rangi1 = 'oq'

    def pazanda(self):
        print('Qoli juddayam shirin')


class Bolasi(Onasi):
    pass


b = Bolasi()

print(b.rangi)
print(b.rangi1)
b.aqilli()
b.pazanda()
