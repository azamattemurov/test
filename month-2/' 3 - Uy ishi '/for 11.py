n = int(input())

yigindi = 0
for i in range(n +1,2*n+1):
    yigindi += i**2

yigindi += n**2+(n+1)**2


print(f'{n} ga teng bo''lgan sonning kvadrati bo'f'lgan {n+1} ga teng sonning yig'f'indisi va {n+2} dan {n*2} gacha sonlarning kvadratlarining yig'f'indisi :{yigindi}')