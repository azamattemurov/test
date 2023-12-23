massiv = input("Massivni elementlarini vergul bilan kiriting: ").split(",")
massiv = [int(element) for element in massiv]


def massivni_osish_tartibida_saralash(massiv):
    massiv.sort()
    return massiv


saralangan_massiv = massivni_osish_tartibida_saralash(massiv)
print(f"Saralangan massiv: {saralangan_massiv}")
