# Day 10 - OOP
# Library Management System

print("Library Management System")


class Book:

    def __init__(self, book_name, author_name, copies):
        self.book_name = book_name
        self.author_name = author_name
        self.copies = copies
        self.available_copies = copies

    def show_book(self):
        print("Book Name:", self.book_name)
        print("Author Name:", self.author_name)
        print("Total Copies:", self.copies)
        print("Available Copies:", self.available_copies)

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies = self.available_copies - 1
            print(self.book_name, "borrowed")
            return True
        else:
            print(self.book_name, "not available")
            return False

    def return_book(self):
        if self.available_copies < self.copies:
            self.available_copies = self.available_copies + 1
            print(self.book_name, "returned")
        else:
            print("This book was not borrowed")


class EBook(Book):

    def __init__(self, book_name, author_name, copies, size):
        super().__init__(book_name, author_name, copies)
        self.size = size

    def show_book(self):
        print("Book Name:", self.book_name)
        print("Author Name:", self.author_name)
        print("Total Copies:", self.copies)
        print("Available Copies:", self.available_copies)
        print("Size:", self.size, "MB")


class User:

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        self.borrowed_books = []

    def show_user(self):
        print("User Name:", self.user_name)
        print("User ID:", self.user_id)
        print("Borrowed Books:", self.borrowed_books)


class Library:

    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(book.book_name, "added to library")

    def add_user(self, user):
        self.users.append(user)
        print(user.user_name, "added as user")

    def show_all_books(self):
        print("\nBooks List")
        for book in self.books:
            book.show_book()
            print()

    def show_all_users(self):
        print("\nUsers List")
        for user in self.users:
            user.show_user()
            print()

    def get_book(self, book_name):
        for book in self.books:
            if book.book_name == book_name:
                return book
        return None

    def get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def borrow(self, user_id, book_name):
        user = self.get_user(user_id)
        book = self.get_book(book_name)

        if user == None:
            print("User not found")
        elif book == None:
            print("Book not found")
        else:
            if book.borrow_book():
                user.borrowed_books.append(book_name)

    def return_book(self, user_id, book_name):
        user = self.get_user(user_id)
        book = self.get_book(book_name)

        if user == None:
            print("User not found")
        elif book == None:
            print("Book not found")
        elif book_name in user.borrowed_books:
            book.return_book()
            user.borrowed_books.remove(book_name)
        else:
            print("User did not borrow this book")


library = Library()

book_name = input("Enter book name: ")
author_name = input("Enter author name: ")
copies = int(input("Enter number of copies: "))

book1 = Book(book_name, author_name, copies)
ebook1 = EBook("Python Basics", "John", 3, 10)

user_name = input("Enter user name: ")
user_id = input("Enter user ID: ")

user1 = User(user_name, user_id)

library.add_book(book1)
library.add_book(ebook1)
library.add_user(user1)

library.show_all_books()
library.show_all_users()

choice = input("Enter borrow or return: ")

if choice == "borrow":
    book_name = input("Enter book name to borrow: ")
    library.borrow(user_id, book_name)

elif choice == "return":
    book_name = input("Enter book name to return: ")
    library.return_book(user_id, book_name)

else:
    print("Wrong choice")

library.show_all_books()
library.show_all_users()