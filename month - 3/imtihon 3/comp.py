class Compyuter:
    def set(self):
        self.comp_list: list[Compyuter] = []

    def __init__(self, nomi, rami, narxi, protsessori):
        self.nomi = nomi
        self.rami = rami
        self.narxi = narxi
        self.protsessori = protsessori

    def malumot(self):
        return f'nomi --> {self.nomi},rami --> {self.rami}, narxi {self.narxi}, protsessori --> {self.protsessori}'


s = Compyuter
