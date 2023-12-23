class Book:
    def __init__(self, nomi, muallifi) -> None:
        self._nomi = nomi
        self._muallifi = muallifi

    @property
    def nomi(self):
        return self._nomi

    @property
    def muallifi(self):
        return self._muallifi

    def __str__(self) -> str:
        return f'{self.muallifi}, {self.nomi}'