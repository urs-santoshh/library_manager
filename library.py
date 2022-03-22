import json

class Library:
    def __init__(self):
        self.lended_books = data
        self.list_of_books = list(self.lended_books.keys())
        
    def display_books(self):
        print("The list of books in the library :")
        for book in self.list_of_books:
            print(book)
            
        print()
    
    def lend_books(self,book,user):
        if book in self.lended_books:
            if self.lended_books[book] == None:
                print("The book is available for you to lend")
                self.lended_books.update({book:user})
                with open("books.json","w",encoding="utf-8") as wb:
                    json.dump(self.lended_books,wb,indent=4,sort_keys=True)
                print("Lending Successful")
            else:
                print("The book is not available now")
                print(f"The book is being used by {self.lended_books[book]}")

        else:
            print("The book is not in the library currently")
        print()
    
    def add_book(self,book):
        self.lended_books.update({book:None})
        with open("books.json","w",encoding="utf-8") as wb:
            json.dump(self.lended_books,wb,indent=4,sort_keys=True)
        print("The book has been added to the library")
        print()

    def return_book(self,book):
        self.lended_books.update({book:None})
        with open("books.json","w",encoding="utf-8") as wb:
            json.dump(self.lended_books,wb,indent=4,sort_keys=True)
        print("Return Successful")
        print(f"The {book} book is available to lend")
        print()

with open("books.json",encoding="utf-8") as b:
        data = json.load(b) 

if __name__ == "__main__": 
    books = Library()
    print("""Welcome to the Python library
1. View list of books
2. Lend books
3. Add book to the library
4. Return book""")
    while True:
        try:
            choice = int(input("Enter your choice :"))
            if choice == 1:
                books.display_books()
            elif choice ==2:
                books.display_books()
                book = input("Enter the name of the book from the list :").casefold()
                user = input("Enter your name :").casefold()
                books.lend_books(book,user)
            elif choice == 3:
                book = input("Enter the name of the book you want to add :").casefold()
                books.add_book(book)
            elif choice == 4:
                book = input("Enter the name of the book you want to return :").casefold()
                books.return_book(book)
            else:
                print("Wrong choice ")
                cont = input("Do you want to continue(Y/N) :").casefold()
                if cont == "y":
                    continue
                else:
                    break
        except ValueError:
            print("Wrong Input")
            cont = input("Do you want to continue(Y/N) :").casefold()
            if cont == "y":
                continue
            else:
                break

    

    
    