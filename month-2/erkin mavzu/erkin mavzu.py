j = 1


def special(res, i):
    if i < 100:
        for amal in ['+', '-', '']:
            special(res + amal + str(i), i + 1)
    elif eval(res) == 10:
        global j
        print(f'{j}. {res} = 100')
        j += 1


special('1', 2)
