#1 = usul
def karrali_elementlar(massiv, K):
    karrali = []

    for element in massiv:
        if element % K == 0:
            karrali.append(element)

    return karrali


massiv = [10, 15, 20, 25, 30, 35]
K = 5

natija = karrali_elementlar(massiv, K)
print(natija)

#2 = usul

k = int(input('Biror bir son kiriting u songa karrali boladigan 5 ta son chiqaraman !'))
s = 0
for i in range(1, 6):
    s = i * k
    print(s)
