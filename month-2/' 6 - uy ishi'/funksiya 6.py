def konsol(son):
    for i in range(2, 11):
        if son % i == 0:
            print(f"{son} = {i} ga qoldiqsiz bo'linadi")
        else:
            print(f'{i}-soni = {son} ga qoldiqsiz bo''linmaydi !')

    if son > 0:
        print(f' Ikkinchi bo\'linma --> {son} // {2} = ', son // 2)
        print(f' Uchinchi bo\'linma --> {son} // {3} = ', son // 3)
        print(f' To\'rtinchi bo\'linma --> {son} // {3} = ', son // 3)
        print(f' Beshinchi bo\'linma --> {son} // {5} =', son // 5)
        print(f' OLtinchi bo\'linma --> {son} // {6} = ', son // 6)
        print(f' Yettinchi bo\'linma --> {son} // {7} = ', son // 7)
        print(f' Sakkizinchi bo\'linma --> {son} // {8} = ', son // 8)
        print(f' To\'qinchi bo\'linma --> {son} // {9} =', son // 9)
        print(f' O\'ningchi bo\'linma --> {son} // {10} = ', son // 10)
    else:
        print(['Error -> siz -0 dan iloji bolsa -10 dan kotta son kiriting !'])


son = int(input("Sonni kiriting: "))
konsol(son)
