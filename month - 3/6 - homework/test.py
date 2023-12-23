from avtodokon import Avtodokon
from avto import Avto

dokon = Avtodokon()

salon1 = Avto('Tracer', 2012, 35000, 'Baxrom')
salon2 = Avto('Malibu', 2005, 25000, 'Azamat')
salon3 = Avto('Gentra', 2006, 20000, 'Sardor')
salon4 = Avto('Nexia 3', 2014, 10000, 'Jamshid')
salon5 = Avto('Spark', 2007, 7000, 'Otabek')
salon6 = Avto('Cobalt', 2009, 9000, 'Aziz')
print()
dokon.addavto(salon1)
dokon.addavto(salon2)
dokon.addavto(salon3)
dokon.addavto(salon4)
dokon.addavto(salon5)
dokon.addavto(salon6)
print()
print('Salonda bor avtomabillar !')
c = dokon.moshina_list
for avto in c:
    print(avto.malumot())
print()
print('Bu 2013 yildan baland avtolar !')
a = dokon.selectavto()
for avto in a:
    print(avto.malumot())
print()
print('Bu 34000 mingdan pas avtolar !')
b = dokon.avtoprice()
for avto in b:
    print(avto.malumot())
print()

