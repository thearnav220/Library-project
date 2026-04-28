import data

def add_book():

    name = input("Enter new book name: ")

    data.books[name] = True

    print("Book added")