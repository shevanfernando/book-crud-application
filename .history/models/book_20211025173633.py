import pandas as pd


class Book:
    def __init__(self, db) -> None:
        self.db = db
        self.cursor = db.cursor(buffered=True)

    def add_book(self) -> None:
        # TODO: complete add book method
        # return the status of book added or not
        status = ""
        print("Enter below details to add books.")
        # get user input
        isbn_no = int(input("ISBN No\t:"))
        book_title = input("Book Title\t:")
        book_author = input("Book Author\t:")
        # check input data empty
        if isbn_no and book_title and book_author:
            is_isbn = "select isbn from book where isbn = %s"
            data = (isbn_no, )
            self.cursor.execute(is_isbn, data)
            if (self.cursor.fetchone()):
                status = "Book already exists under same ISBN number."
            else:
                add_qry = "insert into book (isbn, title, author_name) values (%s, %s, %s)"
                add_data = (isbn_no, book_title, book_author)
                self.cursor.execute(add_qry, add_data)
                self.db.commit()
                status = "Book added successfully!"
        else:
            status = "Invalid data. Try again"
        print(status)

    def list_of_all_books(self) -> None:
        # TODO: complete list books method
        list_qry = "select * from book"
        self.cursor.execute(list_qry)
        list_result = self.cursor.fetchall()
        # print(list_result)
        df = pd.DataFrame(list_result, columns=['ISBN', 'Title', 'Author'])
        print(df.to_string())

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
