import data

def issue_book():

    name = input("Enter book name: ")

    if data.books.get(name) == True:

        student = input("Enter student name: ")
        days = int(input("Enter days: "))

        data.books[name] = False
        data.issued[name] = (student, days)

        print("Book issued")

    else:
        print("Not available")