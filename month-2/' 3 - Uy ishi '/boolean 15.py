a = int(input('son kiriting --->'))
b = int(input('son kiriting --->'))
c = int(input('son kiriting --->'))
if a > 0 and 0 < b and c < 0:
    print(True)
elif a > 0 and 0 > b and c > 0:
    print(True)
elif a < 0 and 0 < b and c > 0:
    print(True)
elif a > 0 and 0 < b and c > 0:
    print(True)
else:
    print(False)