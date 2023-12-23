dict = {
    'qayta ishga tushirish': 'restart',
    'raqam': 'number',
    'manzil': 'addres',
    'takror': 'repeat'

}

while True:
    N = input('Yozasizmi ? ha/ yoq! ')
    if N == 'ha':
        satr = input('Satr yozing ?')
        if satr in list(dict.keys()):
            qiymat = dict[satr]
            print(satr, '=', qiymat.replace("r", "$"))
        else:
            print('uzur yo`q ekan ')
    elif N == 'yoq':
        satr = input('Satr qo\'ing  --> ')
        qiymat = input('Values qo\'shing --> ')
        dict[satr] = qiymat
        print('yangi so\'z qo\'shildi:)')
    else:
        print('Afsuski to\'gri yozmadingiz ! ')

        break
