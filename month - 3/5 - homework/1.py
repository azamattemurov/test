class Avto:
    def __init__(self, narxi, modeli, rangi):
        self.narxi = narxi
        self.module = modeli
        self.rangi = rangi

    @property
    def rangi(self):
        return self.rangi

    @rangi.setter
    def rangi(self, newrang):
        self.rangi = newrang
        print(' Rang o\'zgardi !')


cobalt = Avto
print(cobalt.rangi)
cobalt.rangi = 'qora'
print(cobalt.rangi)


class Student:
    def __init__(self, ism, familya,ball, coin = 0):
        self.ism = ism
        self.familya = familya
        self.coin = coin
        self.ball = ball

    def changekurs(self, new_coin):
        self.coin = new_coin
        print('O\'quvchining coini o\'zgardi !')

    def malumot(self):
        return f'Ismi -> {self.ism}, Familyasi -> {self.familya} , Coini -> {self.coin}, va -> {self.ball}-balli'


salom = Student('azamat', 'sotvoldiyev', 10, 51)
if salom.ball > 0:
    salom.changekurs(30)
    print(salom.ball)
print(salom.malumot())
