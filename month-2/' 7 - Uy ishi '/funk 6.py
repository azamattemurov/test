def Swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


A = int(input())
B = int(input())
C = int(input())
D = int(input())

A, B = Swap(A, B)
C, D = Swap(C, D)

print(f"A = {A}, B = {B}, C = {C}, D = {D}")
