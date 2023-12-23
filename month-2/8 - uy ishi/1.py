# 1 = usul
def toq_sonlar_mas(n):
    massiv = []
    toq_son = 1

    for _ in range(n):
        massiv.append(toq_son)
        toq_son += 2

    return massiv


n = 5

natija = toq_sonlar_mas(n)
print(natija)

# 2 = usul

n = int(input('n---> Son tozing n = ta toq son chiqaraman !'))
for i in range(n + n):
    if i % 2:
        print(i)


