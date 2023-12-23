

try:
    y = [1, 2, 3]
    x = iter(y)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
except:
    print('StopIteration Error bo\'lib qoldi !')
else:
    print('To\'g\'ri ammo Errorsiz zerikarli ')
finally:
    print('Kodimiz tugadi ! ')

# Errorni ko'rmoqchi bolsangiz try va exceptni o'chiring !


