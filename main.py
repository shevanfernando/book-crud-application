import DbAdapter as DB

if __name__ == '__main__':
    name = "Book-CRUD"
    print(f'{name} Application Start...')

    try:
        DB
    except:
        print('DB is not connected.')
