from bookshelf import BookShelf
from book import Book


# shkaf shelf
class Shelf:
    def __init__(self, shelf_code) -> None:
        self._shelf_code = shelf_code
        self.bookshelf_list: list[BookShelf] = [BookShelf(i) for i in range(1, 7)]

    def addbook(self, book: Book, bookshelf_number):
        bookshelf: BookShelf = self.bookshelf_list[bookshelf_number - 1]
        bookshelf.addbook(book)

    def contain(self, book: Book, bookshelf_number):
        bookshelf: BookShelf = self.bookshelf_list[bookshelf_number - 1]
        return bookshelf.contain(book)
