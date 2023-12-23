n=int(input("birinchi sonni kiriting : "))
m=int(input("ikkinchi sonni kiriting : "))
a=0
while 1:
    n=n-m
    a+=1
    if n<m:
        break
print(f"butun qismi {a}")
print(f"qoldiq {n}")
