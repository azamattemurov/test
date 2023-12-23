# Bu ham qoshimcha erkin mavzu
class KyimKechak:
    def __init__(self, nomi, narxi, rangi, sana, razmer) -> None:
        self.nomi = nomi
        self.narxi = narxi
        self.rangi = rangi
        self.sana = sana
        self.razmer = razmer

    def malumot(self):
        return f'Nomi ---> {self.nomi} , Narxi ---> {self.narxi} , Rangi ---> {self.rangi} , Ishlab chiqilgan sanasi ---> {self.sana} , Razmeri ---> {self.razmer}'

print('Birinchi malumot !')

salom = KyimKechak('Kurtka', '300.000 ming', 'Qora', '20-10-2023', 'XXL')
print(salom.malumot())
print('Ikkinchi malumot !')

salom1 = KyimKechak('Etik','250.000 ming','Qora','11-10-2023','41')
print(salom1.malumot())
print('Uchinchi malumot !')

salom1 = KyimKechak('Shim','200.000 ming','Ko\'k','09-10-2023','40')
print(salom1.malumot())