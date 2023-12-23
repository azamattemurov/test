#1 = usul
a = input('Joy tashlab yozing masalan 1 2 3').split()
s = 0
for i in a:
    s += i.isdigit() or '-' == i[0] and i[1:].isdigit()
print(f'{s}  ta dona son bor')
b = s
yigindi = 0
for i in range(1, b+1):
    yigindi += i
print(f' {s} soninng yig\'indisi esa {yigindi} !')
j = s
kopaytmasi = 1
for i in range(1, j+1):
    kopaytmasi *= i
print(f' {s} soninng kopaytmasi esa {kopaytmasi} !')

# 2 = usul
def son_borligini_aniqlash(massiv, son):
    if son in massiv:
        print(f"{son} massivda mavjud.")
    else:
        print(f"{son} massivda mavjud emas.")

def massiv_yigindisi(massiv):
    yigindi = sum(massiv)
    return yigindi

def massiv_kopaytmasi(massiv):
    kopaytma = 1
    for element in massiv:
        kopaytma *= element
    return kopaytma

massiv = []
massiv_size = int(input("Massivning o'lchamini kiriting: "))

for i in range(massiv_size):
    element = int(input(f"Massivning {i+1}-elementini kiriting: "))
    massiv.append(element)

son = int(input("Qidirilayotgan sonni kiriting: "))

son_borligini_aniqlash(massiv, son)
yigindi = massiv_yigindisi(massiv)
kopaytma = massiv_kopaytmasi(massiv)

print(f"Massivning yig'indisi: {yigindi}")
print(f"Massivning ko'paytmasi: {kopaytma}")