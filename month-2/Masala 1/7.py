
n = input()
res ={}
for el in n:
        if el not in res:
            res[el]=1
        else:
            res[el]+=1
for key,val in res.items():

    print(f'{key}:{val}t')
