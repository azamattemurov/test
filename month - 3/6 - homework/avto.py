class Avto:  # getsecondkursi
    def __init__(self, model, year, price, owner):
        self.model = model
        self.year = year
        self.price = price
        self.owner = owner

    def malumot(self):
        return f'modeli ---> {self.model} -- yili ---> {self.year} --uninga narxi {self.price} -- va egasi {self.owner} '
    def __str__(self):
        return self.model
    def __int__(self):
        return self.price

salon1 = Avto('Tracer', 2012, 20000, 'Baxrom')
salon2 = Avto('Malibu', 2005, 17000, 'Azamat')
salon3 = Avto('Gentra', 2006, 12000, 'Sardor')
salon4 = Avto('Nexia 3', 2014, 7000, 'Jamshid')
salon5 = Avto('Spark', 2007, 5000, 'Otabek')
salon6 = Avto('Cobalt', 2009, 8000, 'Aziz')

