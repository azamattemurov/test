def sum():
    yigindi = 0
    a = int(input())
    for i in range(1, a + 1):
        yigindi += i
        print(i, 'son' if i >= 10 else 'raqam')
    print(f' {a} ning yig\'indisi --->  {yigindi} ')


sum()
