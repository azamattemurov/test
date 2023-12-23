l1 = input([1, 2, 3, 4, 5, 6, 7, 8, 4567])
l2 = input([8, 76, 7, 8])
res = []
for el in l1:
    if el in l2 and el not in res:
        res.append(el)
        print(True)


print(res)
