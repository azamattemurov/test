n = int(input("birinchi sonni kiriting : "))
b = int(input("ikkinchi sonni kiriting : "))
a = 0
while 1:
    n = n - b
    a += 1
    if n < b:
        break
print(f"birinchi son - [n] da - [b] soni ->>> {a} marta joylashgan")

