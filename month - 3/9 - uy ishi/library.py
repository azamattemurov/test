from floor import Floor
from book import Book
from bookshelf import BookShelf


# kutubxona
class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.floor_list: list[Floor] = [Floor(1), Floor(2), Floor(3)]

    def get_floor(self, book):
        for floor in self.floor_list:
            for shelf in floor.shelf_list:
                for javon in shelf.bookshelf_list:
                    check = javon.contain(book)
                    if check != None:
                        return f'{floor.floor_number} ---> qavatda joylashgan {book} - kitobi'
        return None

    def get_closet(self, book):
        for floor in self.floor_list:
            for shelf in floor.shelf_list:
                for javon in shelf.bookshelf_list:
                    check = javon.contain(book)
                    if check != None:
                        return f'{shelf._shelf_code} ---> shkafda joylashgan {book} - kitobi'
        return None

    def get_shelf(self, book):
        for floor in self.floor_list:
            for shelf in floor.shelf_list:
                for javon in shelf.bookshelf_list:
                    check = javon.contain(book)
                    if check != None:
                        return f'{javon.javonnumber}---> javonda joylashgan {book} - kitobi'
        return None

    def find(self, book):
        for floor in self.floor_list:
            for shelf in floor.shelf_list:
                for javon in shelf.bookshelf_list:
                    check = javon.contain(book)
                    if check != book.nomi and check != book.muallifi:
                        return f'{book.nomi} ---> kitobining yozuvchisi ---> {book.muallifi}'
            return None

    def get_books(self, floor_number, shelf_number):
        floor: Floor = self.floor_list[floor_number - 1]
        floor.get_books(shelf_number)

    def addbook(self, floor_number, shelf_number, bookshelf_number, book):
        floor: Floor = self.floor_list[floor_number - 1]
        floor.addbook(book, shelf_number, bookshelf_number)

    def contain(self, floor_number, shelf_number, bookshelf_number, book):
        floor: Floor = self.floor_list[floor_number - 1]
        return floor.contain(book, shelf_number, bookshelf_number)
