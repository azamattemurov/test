import s


class Technology:
    def tehno(self):
        print('Hozirgi zamonda o\'rni katta')


class Smartphones(Technology):
    def __init__(self, smart, speed, good):
        self.__smart = smart
        self._speed = speed
        self.good = good


# propertysz qildim ozimga qulay edida uzur ustoz !
def changesmart(self, new_smart):
    self.__smart = new_smart
    print('1 - yildan so\'ng yana smartphonening ajoyib va zo\'r versiasilari chiqadi !')


def malumot(self):
    return f'Uning aqiligi--> {self.__smart}, tezligi --> {self._speed}, u narsa qanaqa ---> {self.good}'


class Gadgets(Technology):
    def __init__(self, smart1, beatiful, qulay):
        self.__smart1 = smart1
        self._beatiful = beatiful
        self.qulay = qulay

    # propertysz qildim ozimga qulay edida uzur ustoz !
    def changesmart(self, new_smart):
        self.__smart = new_smart
        print('1 - yildan so\'ng yana gatgetsning ajoyib va zo\'r versiasilari chiqadi !')

    def malumot(self):
        return f'Uning aqiligi --> {self.__smart1}, ko\'rinishi --> {self._beatiful}, u narsa qulaymi ---> {self.qulay}'


print('Smartphones !')
print()
c = Smartphones('Juddayam aqilli', 'Ha tez ammo smartphonga qarab', 'Juddayam ajoyib')

print()
print('Gatgets !')
print()
b = Gadgets('Juddayam aqilli', 'Ha albatta ammo gadgetsga qarab', 'Judda qulay')
print(b.malumot())
print(b.changesmart(''))
print(b.qulay)
