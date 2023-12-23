a = input()
s = []
for i in a:
    if i.isalpha():
        s += str(i)
print('a ning harflari --- >', s)
x = 0
for i in a:
    if i.isdigit():
        x += int(i) ** 2
print('a ning kubi --- > ', [x])
