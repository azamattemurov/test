mydict = {'1 * 1': 1,
          '1 * 2': 2,
          '1 * 3': 3,
          '1 * 4': 4,
          '1 * 5': 5,
          '1 * 6': 6,
          '1 * 7': 7,
          '1 * 8': 8,
          '1 * 9': 9,
          '1 * 10': 10

          }
while True:
    N = input('Hisoblaylikmi ? ha/ yoq! ')
    if N == 'ha':
        son = input('Aynan qaysi son ?')
        if son in list(mydict.keys()):
            karra = mydict[son]
            print(son, '=', karra)
        else:
            print('uzur yo`q ekan ')
    elif N == 'yoq':
        son = input('karrani qo\'shing --> ')
        karra = input('Javobini qo\'shing --> ')
        mydict[son] = karra
        print('yangi karra qo\'shildi:)')
    else:
        print('afsuski siz bilan o`yinimiz tugadi:) ')

        break
