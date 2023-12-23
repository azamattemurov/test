#1 = usul
def toq_songacha_yigindi(massiv):
    toq_songacha = 0
    for element in massiv:
        if element % 2 != 0:  # toq sonlarni tekshiramiz
            toq_songacha += element
    return toq_songacha

massiv = []
massiv_size = int(input("Massivning o'lchamini kiriting: "))

for i in range(massiv_size):
    element = int(input(f"Massivning {i+1}-elementini kiriting: "))
    massiv.append(element)

toq_songacha = toq_songacha_yigindi(massiv)
print(f"Toq songacha yig'indi: {toq_songacha}")
print('Bunda faqat toq sonlarini hisobladim !')

#2 = usul

n = int(input('n---> Son tozing !'))
yigindi = 0
if n % 2:
    for i in range(n + 1):
        yigindi += i
    print(f'{yigindi} bu toq soning yig\'indisi !')
else:
    yigindi1 = 0
    for i in range(n):
        yigindi1 += i
    print(f'{yigindi1-1} bu esa toq soning yig\'indisi 1 va oxirgi son yoq !')
print('Bunda juft va toq sonlarni hisobladim !')