from logging import log
from DbAdapter import db
from models.login import Login
from dummy_data import DummyData

if __name__ == '__main__':
    name = "Book-CRUD"
    print(f'{name} Application Start...')

    user_is_logged: bool = False

    try:
        dummy = DummyData(db)

        if not user_is_logged:
            login = Login(db)
            user_is_logged = login.login()

        # commit changes
        db.commit()

    except Exception as e:
        print(e)
