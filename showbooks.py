import data

def show_books():

    for b in data.books:

        if data.books[b]:
            print(b, "Available")

        else:
            print(b, "Issued")