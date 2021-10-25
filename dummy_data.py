class DummyData:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor(buffered=True)
        self.create_tables()
        self.insert_dummy_data()

    def create_tables(self):
        # create user table
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS user (username VARCHAR(256) PRIMARY KEY, password VARCHAR(256))')

        # create book table
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS book (isbn int AUTO_INCREMENT PRIMARY KEY,title VARCHAR(256), author_name VARCHAR(256))')

    def insert_dummy_data(self):
        # user table dummy data insert
        self.cursor.execute('SELECT * FROM user')
        if len(self.cursor.fetchall()) == 0:
            qry = 'INSERT INTO user(username, password) VALUES(%s, %s)'
            data = [('admin', 'admin'), ('user', 'user')]
            self.cursor.executemany(qry, data)
            print('dummy data insert to user table')
            # save users
            self.db.commit()

        # book table dummy data insert
        self.cursor.execute('SELECT * FROM book')
        if len(self.cursor.fetchall()) == 0:
            qry = "INSERT INTO book(title, author_name) VALUES(%s, %s)"
            data = [('ABSALOM, ABSALOM!', 'WILLIAM FAULKNER'),
                    ('A TIME TO KILL', 'JOHN GRISHAM'),
                    ('THE HOUSE OF MIRTH', 'EDITH WHARTON'),
                    ('EAST OF EDEN', 'JOHN STEINBECK'),
                    ('THE SUN ALSO RISES', 'ERNEST HEMINGWAY'), ]

            self.cursor.executemany(qry, data)

            print('dummy data insert to book table')

            # save book data
            self.db.commit()
