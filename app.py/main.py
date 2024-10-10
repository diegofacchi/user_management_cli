import mysql.connector
from time import sleep

def print_colored_text(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def connect_to_db():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='user_management_cli'
    )

    except mysql.connector.Error as err:
        print_colored_text(f"Error: {err}", '31')
        exit(1)


def add_user():
    name =  input("Enter the user's name: ").strip().title()
    email = input("Enter the user's email: ").strip()
    password = input("Enter the user's password: ").strip()
    cursor.execute("INSERT INTO users(name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    db.commit()
    print_colored_text("User added successfully!", '32')


def list_users():
    pass


def edit_users():
    pass


def delete_user():
    pass


def menu():
    while True:
        print_colored_text("\nUser Management System", '34')
        print_colored_text("1. Add user", '32')
        print_colored_text("2. List users", '33')
        print_colored_text("3. Edit users", '35')
        print_colored_text("4. Delete user", '36')
        print_colored_text("5. Exit", '31')

        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            edit_users()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            sleep(0.5)
            print_colored_text("Exiting the system...", '31')
            break
        else:
            print_colored_text("Invalid option. Please try again.", '31')

db = connect_to_db()
cursor = db.cursor()
menu()