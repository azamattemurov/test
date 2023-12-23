m = int(input())
a = [23, 2, 4, 543, 55]
a[1] = m

a.remove(min(a))
a.remove(max(a))
print(a)

