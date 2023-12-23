from comp import Compyuter


class Comp1:
    def __init__(self):
        self.comp_list: list[Compyuter] = []
    def addcomp(self, comp: Compyuter):
        self.comp_list.append(comp)
        print()
    def selectram(self):
        res = []
        for compyuter in self.comp_list:
            if compyuter.rami > 4 and compyuter.rami < 16:
                res.append(compyuter)
        return res

