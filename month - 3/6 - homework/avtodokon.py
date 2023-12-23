from avto import Avto


class Avtodokon:
    def __init__(self):
        self.moshina_list: list[Avto] = []

    def addavto(self, avto: Avto):
        self.moshina_list.append(avto)
        print('Avto qo\'shildi !')

    def getstudents(self):
        return self.moshina_list

    def selectavto(self):
        res = []
        for avto in self.moshina_list:
            if avto.year > 2013:
                res.append(avto)
        return res

    def avtoprice(self):
        resalt = []
        for avto in self.moshina_list:
            if avto.price <= 34000:
                resalt.append(avto)
        return resalt
