a, b = input()
if a > b:
    print(a,'teng emas !')
elif b > a:
    print(b, 'teng emas')
else:
    print('0- teng bolganligi uchun' , a,'a =soni>>',b,' b =soni')
n = int(input())
sum = 0
for i in range(n, n * 2 + 1):
    sum += i * i
    print(sum)
