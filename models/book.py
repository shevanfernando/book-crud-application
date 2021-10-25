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
        id = input('Book isbn: \n')

        qry = 'DELETE FROM book WHERE isbn = %s'

        cd = self.cursor.execute(qry, (id,))

        self.db.commit()

        print(f'Book with isdn : {id} delete { cd == None and "failed"}')

    def __get_book_by_id(self) -> any:
        id = input('Book isdn: \n')

        qry = 'SELECT isbn, title, author_name FROM book WHERE isbn = %s'

        self.cursor.execute(qry, (id,))

        return self.cursor.fetchone()
