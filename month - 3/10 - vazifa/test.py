from errorWord import ErrorWord
mylist = ['a','b','c','d','h','j','k','l']
for i in mylist:
    if i == 'j':
        raise ErrorWord
    else:
        print(i)