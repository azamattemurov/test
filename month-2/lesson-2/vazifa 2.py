set1={10,20,30,40,50}
set2={30,40,50,60,70}
res=[]
for el in set1:
       if el in set2:
           res.append(el)
print(res)