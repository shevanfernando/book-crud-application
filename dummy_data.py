class DummyData:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor(buffered=True)
        self.create_tables()
        self.insert_dummy_data()

    def create_tables(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS user (username VARCHAR(256) PRIMARY KEY, password VARCHAR(256))')

    def insert_dummy_data(self):
        # user table data insert
        self.cursor.execute('SELECT * FROM user')
        if len(self.cursor.fetchall()) == 0:
            user_qry = 'INSERT INTO user(username, password) VALUES(%s, %s)'
            user_data = [('admin', 'admin'), ('user', 'user')]
            self.cursor.executemany(user_qry, user_data)
            print('dummy data insert to user table')

        self.db.commit()
