# 1 va 3 masala bitta .py fileda !
class Student:
    # bu init va selfga bir misol
    def __init__(self, ID, ismi, familyasi, kurs) -> None:
        self.ID = ID
        self.ismi = ismi
        self.familyasi = familyasi
        self.kurs = kurs

    def changekurs(self, new_kurs):
        self.kurs = new_kurs
        print('1 yildan so\'ng kursni bitirib !')

    def malumot(self):
        return f'ID num -> {self.ID}, Ismi -> {self.ismi} , Familya -> {self.familyasi}, va -> {self.kurs}-kursdaa'


oquvchi = Student(655, 'Azamat', 'Timurov', 1)
print(oquvchi.malumot())
oquvchi.changekurs('Endi esa 2 - kurs bo\'ldi')
print(oquvchi.kurs)
oquvchi.changekurs('Endi esa 3 - kurs bo\'ldi')
print(oquvchi.kurs)
oquvchi.changekurs('Endi esa 4 - kurs bo\'ldi')
print(oquvchi.kurs)
oquvchi.changekurs('Oxiri o\'qishni tugatdi tabriklaymiz !')
print(oquvchi.kurs)
