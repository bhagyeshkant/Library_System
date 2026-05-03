import os
from models import Book

class Library:
    def __init__(self):
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists("books.txt"):
                with open("books.txt", "r") as f:
                    for line in f:
                        data = line.strip().split(",")
                        book = Book(data[0], data[1], data[2])
                        book.is_issued = data[3] == "True"
                        self.books.append(book)
        except Exception as e:
            print("Error loading books:", e)

    def save_data(self):
        try:
            with open("books.txt", "w") as f:
                for book in self.books:
                    f.write(f"{book.book_id},{book.title},{book.author},{book.is_issued}\n")
        except Exception as e:
            print("Error saving data:", e)

    def add_book(self, book_id, title, author):
        self.books.append(Book(book_id, title, author))
        print("Book added successfully!")

    def view_books(self):
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(book.book_id, book.title, book.author, status)

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print("Book issued successfully!")
                else:
                    print("Book already issued!")
                return
        print("Book not found!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned!")
                else:
                    print("Book was not issued!")
                return
        print("Book not found!")
