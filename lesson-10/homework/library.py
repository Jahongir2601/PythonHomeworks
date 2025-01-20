class BookNotFoundException(Exception):
    pass
class BookAlreadyBorrowedException(Exception):
    pass
class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"
    
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book:Book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"Member '{self.name}' can't borrow more than 3 books")
        if book.borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title} is already borrowed")
        self.borrowed_books.append(book)
        book.borrowed = True

    def return_book(self, book:Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.borrowed = False
        else:
            print(f"{book.title} is not borrowed by {self.name}")

    def __str__(self):
        books_borrowed = ", ".join(book.title for book in self.borrowed_books)
        return f"Member: {self.name}, Borrowed books: [{books_borrowed}]" 
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by '{author}' added to the library")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Member '{name}' added to the library")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library")
    
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member 
        print(f"Member '{name}' not found")
        return None
    
    def borrow_book(self, member_name, book_title):
        try:
            member = self.find_member(member_name)
            if not member:
                return
            book = self.find_book(book_title)
            member.borrow_book(book)
            print(f"'{book_title} borrowed by {member_name}'")
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(f"Error: {e}")
        
    def return_book(self, member_name, book_title):
        try:
            member = self.find_member(member_name)
            if not member:
                return
            book = self.find_book(book_title)
            member.return_book(book)
            print(f"'{book_title} returned by {member_name}'")
        except BookNotFoundException as e:
            print(f"Error: {e}")

    def list_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

    def list_members(self):
        print("Members in the library:")
        for member in self.members:
            print(member)

if __name__ == "__main__":
    library = Library()
    while True:
        print("\nLibrary application menu")
        print("1. Add book")
        print("2. Add member")
        print("3. Borrow book")
        print("4. Return book")
        print("5. List books")
        print("6. List members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        
        elif choice == "2":
            name = input("Enter member name: ")
            library.add_member(name)

        elif choice == "3":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            library.borrow_book(member_name, book_title)

        elif choice == "4":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            library.return_book(member_name, book_title)
        
        elif choice == "5":
            library.list_books()

        elif choice == "6":
            library.list_members()

        elif choice == "7":
            break