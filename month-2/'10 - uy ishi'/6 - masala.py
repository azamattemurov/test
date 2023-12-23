n = input()
if len(n) >= 3:
    if n.count('4'):
        print(n.__add__('7'))
    else:
        print(n.__add__('ing'))
elif len(n) <= 3:
    print()


