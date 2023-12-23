# Bu qoshimcha erkin mavzu
class Odam:
    def __init__(self, millat, yosh, til, ish) -> None:
        self.millat = millat
        self.til = til
        self.yosh = yosh
        self.ish = ish

    def malumot(self):
        return f'Millati ---> {self.millat} , Tili ---> {self.til} , Yoshi ---> {self.yosh} , Ish joyi ---> {self.ish}'


son = int(input("Son kiriting -->"))
for i in range(son):
    salom = Odam('O\'zbek', '23', 'O\'zbek tili', 'Harbiy')
    print(salom.malumot())

