# Tub sonni aniqlash !
def isPrime( son):
    if son < 2:
        for i in range(2, son):
            if son % i == 0:
                return False
        return True


number = int(input())
if isPrime(number):
    print('Tub son')
else:
    print('Tub emas')
