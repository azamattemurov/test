def qoshish():
    k = int(input())
    r = int(input())
    if 1 < r and r < 9:
        res = str(r) + str(k)
        print(res)
    else:
        print(f'{r}-[ERROR] = 1-dan kotta va 9-dan pas son kiriting ! ')


qoshish()
