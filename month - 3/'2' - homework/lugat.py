with open('son.txt', 'r') as file:
    while True:
        N = input('Hisoblaylikmi ? ha/ yoq')
        if N == 'ha':
            m = input('So\'z kiriting :')
            for qator in file.readlines():
                if m in qator:
                    print(qator)
                    break
            else:
                print('Hato afsus ')

            with open('son.txt', 'a') as file:
                soz = input('Va yangi so\'z kiriting :')
                tarjima = input('Javobini qo\'shing --> ')
                line = f'{soz},{tarjima}\n'
                file.write(line)
                file.write('\n')
                print('Raxmat yangi lug\'at qo\'shildi:)')
        else:
            print('afsuski siz bilan o`yinimiz tugadi:) ')
        break
