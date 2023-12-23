
n = int(input())
a = [23, 4, 5, 6, 123]
a[1] = n
summa = 0
for i in a:
    summa += i
print('arifmetik --> ', summa/len(a))
