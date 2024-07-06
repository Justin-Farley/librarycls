from db_connector import *

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            book_operations_menu()
        elif choice == '2':
            user_operations_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def book_operations_menu():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book by title")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter title of the book: ")
            author_id = int(input("Enter author ID: "))
            genre_id = int(input("Enter genre ID: "))
            add_book(title, author_id, genre_id)
        elif choice == '2':
            book_id = int(input("Enter book ID to borrow: "))
            borrow_book(book_id)
        elif choice == '3':
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)
        elif choice == '4':
            title = input("Enter title to search: ")
            search_books_by_title(title)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def user_operations_menu():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. List all users")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name of the user: ")
            email = input("Enter email of the user: ")
            add_user(name, email)
        elif choice == '2':
            fetch_all_users()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main_menu()
    finally:
        close_connection()
