class Library :
    def __init__(self,book):
        self.book = book

    def list_books(self):
        for books in self.book :
            print(books)

    def borrow_books(self,borrow_book):
        if borrow_book in self.book:
            print('Get Your book now')
            self.book.remove(borrow_book)
        else:
            print("Book Not available in the library")

    def return_book(self,return_book):
        print("You Have returned the book")
        self.book.append(return_book)

list1 = ["C", "C++", "Python", "Java"]
o = Library(list1)

while True :
    msg = '''
    1. Display Book
    2. Borrow Book
    3. Return Book
    '''
    print(msg)
    ch = int(input("Enter Your Choice : "))
    if ch == 1 :
        o.list_books()
    elif ch == 2 :
        new = input("Enter the book name : ")
        o.borrow_books(new)
    elif ch == 3:
        new = input("Enter the book name : ")
        o.return_book(new)
    else:
        print("Invalid Attempt. Thanks for Visiting , Come again")
        quit()