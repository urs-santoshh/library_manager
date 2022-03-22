import json

class Library:
    def __init__(self):
        self.lended_books = data
        self.list_of_books = list(self.lended_books.keys())
        
    def display_books(self):
        print("The list of books in the library :")
        for book in self.list_of_books:
            print(book)
    
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
    
    def add_book(self,book):
        self.lended_books.update({book:None})
        with open("books.json","w",encoding="utf-8") as wb:
            json.dump(self.lended_books,wb,indent=4,sort_keys=True)
        print("The book has been added to the library")

    def return_book(self,book):
        self.lended_books.update({book:None})
        with open("books.json","w",encoding="utf-8") as wb:
            json.dump(self.lended_books,wb,indent=4,sort_keys=True)
        print("Return Successful")
        print(f"The {book} book is available to lend")

with open("books.json",encoding="utf-8") as b:
        data = json.load(b) 

if __name__ == "__main__": 
    books = Library()
    books.add_book("Python is fun")
    
    

    
    