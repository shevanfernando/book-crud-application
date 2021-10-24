
class Book:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = db.cursor(buffered=True)

    def add_book(self) -> None:
        # TODO: complete add book method
        pass

    def list_of_all_books(self) -> None:
       # TODO: complete list books method
        pass

    def edit_book(self) -> None:
       # TODO: complete edit book method
        pass

    def remove_book(self) -> None:
       # TODO: complete remove book method
        pass

    def __get_book_by_id(self) -> None:
        # TODO: complete get book method
        pass
