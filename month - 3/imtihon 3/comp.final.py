from compedit import Comp1
from comp import Compyuter

dokon = Comp1()
w1 = Compyuter('asus', 5, 9.000, 4)
w2 = Compyuter('lenova', 15, 6.000, 3)
w3 = Compyuter('apple', 17, 12.000, 5)
w4 = Compyuter('linox', 3, 7.000, 4)
print('')
dokon.addcomp(w1)
dokon.addcomp(w2)
dokon.addcomp(w3)
dokon.addcomp(w4)
c = dokon.selectram()
for comp in c:
    print(comp.malumot())
