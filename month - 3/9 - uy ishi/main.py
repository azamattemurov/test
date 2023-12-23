from book import Book
from library import Library

library = Library('Najot ta\'lim hadra filiali')

kitob1 = Book('odamiylik mulki', 'Tohir Malik')

library.addbook(1, "C23", 6, kitob1)
library.addbook(1,'C23',1,kitob1)
library.get_books(1,'C23')
print(library.get_floor(kitob1))
print(library.get_closet(kitob1))
print(library.get_shelf(kitob1))
#  find da esa kitob1 = Book dagi nomi yoki muallifini o'zgartiring !
print(library.find(kitob1))

library.contain(1, "C2", 3, kitob1)
#print(kitob1.muallifi)
#print(kitob1.nomi)
