import mysql.connector

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="Supersaiyan40",
    database="library_db"
)

db_cursor = db_connection.cursor()

def close_connection():
    db_cursor.close()
    db_connection.close()

def add_book(title, author_id, genre_id):
    try:
        sql = "INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s)"
        val = (title, author_id, genre_id)
        db_cursor.execute(sql, val)
        db_connection.commit()
        print("Book added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def borrow_book(book_id):
    try:
        sql = "UPDATE books SET is_borrowed = TRUE WHERE book_id = %s"
        val = (book_id,)
        db_cursor.execute(sql, val)
        db_connection.commit()
        print("Book borrowed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def return_book(book_id):
    try:
        sql = "UPDATE books SET is_borrowed = FALSE WHERE book_id = %s"
        val = (book_id,)
        db_cursor.execute(sql, val)
        db_connection.commit()
        print("Book returned successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def search_books_by_title(title):
    try:
        sql = "SELECT * FROM books WHERE title LIKE %s"
        val = ('%' + title + '%',)
        db_cursor.execute(sql, val)
        books = db_cursor.fetchall()
        for book in books:
            print(book)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_user(name, email):
    try:
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        db_cursor.execute(sql, val)
        db_connection.commit()
        print("User added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def fetch_all_users():
    try:
        db_cursor.execute("SELECT * FROM users")
        users = db_cursor.fetchall()
        for user in users:
            print(user)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_author(name, nationality):
    try:
        sql = "INSERT INTO authors (name, nationality) VALUES (%s, %s)"
        val = (name, nationality)
        db_cursor.execute(sql, val)
        db_connection.commit()
        print("Author added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def fetch_all_authors():
    try:
        db_cursor.execute("SELECT * FROM authors")
        authors = db_cursor.fetchall()
        for author in authors:
            print(author)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def search_authors_by_name(name):
    try:
        sql = "SELECT * FROM authors WHERE name LIKE %s"
        val = ('%' + name + '%',)
        db_cursor.execute(sql, val)
        authors = db_cursor.fetchall()
        for author in authors:
            print(author)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
