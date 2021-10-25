from DbAdapter import db
from dummy_data import DummyData
from models.login import Login
from models.book import Book


def quite() -> None:
    choice = input('Do you want to exit? [y/n] \n').upper() == 'Y'
    if choice:
        print('Quitting...'),
        exit()


def switch(choice: str):
    switcher = {
        '1': book.add_book(),
        '2': book.list_of_all_books(),
        '3': book.edit_book(),
        '4': book.remove_book(),
        '9': quite(),
    }
    return switcher.get(choice, 'Invalid choice...')


if __name__ == '__main__':
    name = "Book-CRUD"
    print(f'{name} Application Start...')

    user_is_logged: bool = False

    try:
        dummy = DummyData(db)

        if not user_is_logged:
            login = Login(db)
            user_is_logged = login.login()

        book = Book(db)

        while (True):
            print('[1] Add new book')
            print('[2] List all books')
            print('[3] Edit book')
            print('[4] Remove book')
            print('[9] Exit')

            choice = input('Select: ')

            print(switch(choice))

        # commit changes
        db.commit()

    except Exception as e:
        print(e)
