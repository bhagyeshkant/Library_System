# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:08:25 2026

@author: Bhagyesh Kant
"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


        
import os

class Library:
    def __init__(self):
        self.books = []
        self.users = []
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
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")
        
    def view_books(self):
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(book.book_id, book.title, book.author, status)
            
    def issue_book(self, book_id):
        try:
            for book in self.books:
                if book.book_id == book_id:
                    if not book.is_issued:
                        book.is_issued = True
                        print("Book issued successfully!")
                        return
                    else:
                        print("Book already issued!")
                        return
            print("Book not found!")
        except Exception as e:
            print("Error:", e)
    
    def return_book(self, book_id):
        try:
            for book in self.books:
                if book.book_id == book_id:
                    if book.is_issued:
                        book.is_issued = False
                        print("Book returned!")
                        return
                    else:
                        print("Book was not issued!")
                        return
            print("Book not found!")
        except Exception as e:
            print("Error:", e)

def main():
    lib = Library()

    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            b_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(b_id, title, author)

        elif choice == "2":
            lib.view_books()

        elif choice == "3":
            b_id = input("Enter Book ID: ")
            lib.issue_book(b_id)

        elif choice == "4":
            b_id = input("Enter Book ID: ")
            lib.return_book(b_id)

        elif choice == "5":
            lib.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()
    
        
        
 
