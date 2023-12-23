# otasidan bolasiga vorislik !
class Otasi:
    rangi = 'qora'
    def smart(self):
        print('Juddayam tez')


class Bolasi(Otasi):
    pass


b = Bolasi()


print(b.rangi)
b.smart()
