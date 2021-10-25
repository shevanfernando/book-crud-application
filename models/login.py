from mysql.connector import errors, errorcode


class LoginDTO:
    username: str
    password: str

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Login:
    def __init__(self, db: any) -> None:
        self.db = db
        self.cursor = db.cursor(buffered=True)
        self.is_Not_logging: bool = True

    def login(self) -> bool:

        while(self.is_Not_logging):
            print('[1] Exists user')
            print('[2] New user')

            choice = input('Select: \n')

            if choice == '1':
                data = self.__get_data()

                qry = 'SELECT username FROM user WHERE username=%s AND password=%s'

                self.cursor.execute(
                    qry, (data.username, data.password))

                if len(self.cursor.fetchall()) != 0:
                    print('Logging success...')
                    self.is_Not_logging = False
                    return True

                print('Loggin failed...')

            elif choice == '2':
                self.new_user()
            else:
                print('Your choice is invalid... \n Try again...\n')

    def new_user(self) -> None:
        print('Welcome...')

        while True:
            data = self.__get_data()

            qry = 'INSERT INTO user(username, password) VALUES(%s, %s)'

            try:
                self.cursor.execute(qry, (data.username, data.password))

                # save new user
                self.db.commit()

                print(f'{data.username}, new account create successful... \n')

                self.login()
                break
            except errors.IntegrityError as e:
                if e.errno == errorcode.ER_DUP_ENTRY:
                    print(f'{data.username}, already taken... \n Try again...\n')
                else:
                    raise e

    def __get_data(self) -> LoginDTO:
        username = input('Enter username: \n')
        password = input('Enter password: \n')
        return LoginDTO(username, password)
