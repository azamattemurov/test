# 1 va 3 chi masalani yarmi bitta .py fileda !
# 3. Private , Protected va publiclarning ko'rinichi !
__narxi = '200000$'  # bu private
_model = 'Tracker'  # bu protected
rangi = 'Qora'  # bu public


# va class yaratamiz !
class Avtomobil:
    __narxi = '200000$'
    _model = 'Tracker'
    rangi = 'Qora'

    # 1. instance metod ga misol !
    def yurish(self):
        print('Moshina yura oladi')

    def signal(self):
        print('Moshina signal chala oladi')

    def toxtash(self):
        print('Moshina toxtay oladi ')


avto1 = Avtomobil()
print('Moshinani malumotlari !')
# print(avto1.__narxi - afsuski private ni chaqirib bolmaydi !)
print(avto1._model)
print(avto1.rangi)
print('Moshina nimalar qila oladi ?')
avto1.yurish()
avto1.signal()
avto1.toxtash()
