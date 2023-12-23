a = input()
res = ''
for i in a:
    if i == '4':
        res += '7'
    elif i == '7':
        res += '4'
    else:
        res += i

print(res)