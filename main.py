from library import Library

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
