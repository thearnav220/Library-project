import data

def return_book():

    name = input("Enter book name: ")

    if name in data.issued:

        extra = int(input("Extra days: "))

        fine = extra * 10

        print("Fine =", fine)

        data.books[name] = True
        del data.issued[name]

    else:
        print("Book not issued")