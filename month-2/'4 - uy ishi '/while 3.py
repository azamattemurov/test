n=int(input("birinchi sonni kiriting : "))
b=int(input("ikkinchi sonni kiriting : "))
a=0
while 1:
    n=n-b
    a+=1
    if n<b:
        break
print(f"butun qismi {a}")
print(f"qoldiq {n}")
