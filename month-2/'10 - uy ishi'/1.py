import random

res = []
for i in range(5):
    res.append(random.randint(60, 65))
print('Bu ishlashning oxirgi yoshlari =',set(res))

for i in range(3):
    res.append(random.randint(65, 76))
print('Bu esa ishlashga loyiq emas =',set(res))

for i in range(3):
    res.append(random.randint(18, 65))
print('Bu esa ishlashga loyiq =',set(res))

