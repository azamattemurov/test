from shelf import Shelf
from book import Book
from bookshelf import BookShelf


# qavat froor
class Floor:
    def __init__(self, floor_number) -> None:
        self.floor_number = floor_number
        self.shelf_list: list[Shelf] = [Shelf('C' + str(i)) for i in range(1, 31)]

    def get_books(self, shelf_number):
        shelf: Shelf = self.shelf_list[int(shelf_number[1:]) - 1]
        javon: BookShelf
        for javon in shelf.bookshelf_list:
            print(f'Javon --- > {javon.javonnumber}')
            for kitob in javon.booklist:
                print(kitob)


    def addbook(self, book: Book, shelf_number, bookshelf_number):
        index_shelflist = int(shelf_number[1:])
        shelf: Shelf = self.shelf_list[index_shelflist - 1]
        shelf.addbook(book, bookshelf_number)

    def contain(self, book: Book, shelf_number, bookshelf_number):
        index_shelflist = int(shelf_number[1:])
        shelf: Shelf = self.shelf_list[index_shelflist - 1]
        return shelf.contain(book, bookshelf_number)
