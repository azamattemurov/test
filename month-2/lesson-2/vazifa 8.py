set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
def a():
    return 10,20,30,40,50
b = list(a())
b.remove(10)
b.remove(20)
b.remove(30)
print(set1 & set2)