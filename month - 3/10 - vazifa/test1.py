from worderror1 import Errors
mylist = [1,2,3,4,5,6,7,8,9,10]
res = []
for i in mylist:
    res.append(i*2) # = 4 chiqsa error
    if res == '18':
        raise Errors
    else:
        print(i)
