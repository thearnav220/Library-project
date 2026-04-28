from showbooks import show_books
from issuebook import issue_book
from returnbook import return_book
from addbook import add_book

while True:

    print("\n1 Show Books")
    print("2 Issue Book")
    print("3 Return Book")
    print("4 Add Book")
    print("5 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        show_books()

    elif ch == "2":
        issue_book()

    elif ch == "3":
        return_book()

    elif ch == "4":
        add_book()

    elif ch == "5":
        break

    else:
        print("Wrong choice")