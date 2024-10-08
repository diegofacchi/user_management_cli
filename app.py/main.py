import mysql.connector


def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='user_management_cli'
    )


def add_user():
    pass


def list_users():
    pass


def edit_users():
    pass


def delete_user():
    pass


def menu():
    pass

db = connect_to_db()
cursor = db.cursor()
menu()