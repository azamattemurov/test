try:
 with open('abc.txt', 'w', encoding='abc') as my_file:
    my_file.write('first' + '\n')
    my_file.write('second' + '\n')
    my_file.write('third' + '\n')
except:
    print("Bu esa LookupError")

# Errorni ko'rmoqchi bolsangiz try va exceptni o'chiring !