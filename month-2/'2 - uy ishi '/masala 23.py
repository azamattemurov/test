N = int(input('N (sekundlarda kiriting !) --> '))

soat = N // 3600
minut = N // 60
sekund = N % 3600

print(f'{N} sekund ichida {soat} soat va {minut} minut va {sekund} sekund bor')