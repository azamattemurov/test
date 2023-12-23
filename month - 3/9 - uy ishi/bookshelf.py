from book import Book


# book shelf javon
class BookShelf:
    def __init__(self, qavat_id) -> None:
        self._qavat_id = qavat_id
        self.booklist: list[Book] = []
    @property
    def javonnumber(self):
        return self._qavat_id

    def addbook(self, book: Book):
        if len(self.booklist) >= 10:
            print('Afsus kitob sig\'madi')
        else:
            self.booklist.append(book)
            print('Ha kitob qo\'shildi')
            print(self.booklist)

    def contain(self, enter_book: Book):
        for book in self.booklist:
            if book.muallifi == enter_book.muallifi and book.nomi == enter_book.nomi:
                return book
        return None