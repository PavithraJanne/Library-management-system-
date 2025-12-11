class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.book_id} | {self.title} by {self.author} | {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"{self.member_id} | {self.name} | Borrowed: {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book added: {book.title}")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Member added: {member.name}")

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found!")
            return
        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.is_available:
            print("Book is already borrowed!")
            return

        book.is_available = False
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id, book_id):
        if member_id not in self.members:
            print("Member not found!")
            return

        member = self.members[member_id]
        book = self.books.get(book_id)

        if book not in member.borrowed_books:
            print("This book was not borrowed by the member!")
            return

        member.borrowed_books.remove(book)
        book.is_available = True
        print(f"{member.name} returned '{book.title}'")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books.values():
            print(book)

    def display_members(self):
        print("\n--- Members List ---")
        for member in self.members.values():
            print(member)


def menu():
    library = Library()

    while True:
        print("""
===== LIBRARY MANAGEMENT MENU =====
1. Add Book
2. Add Member
3. Borrow Book
4. Return Book
5. Display All Books
6. Display All Members
7. Exit
====================================""")

        choice = input("Enter choice: ")

        if choice == "1":
            bid = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            library.add_book(Book(bid, title, author))

        elif choice == "2":
            mid = input("Member ID: ")
            name = input("Name: ")
            library.add_member(Member(mid, name))

        elif choice == "3":
            mid = input("Member ID: ")
            bid = input("Book ID: ")
            library.borrow_book(mid, bid)

        elif choice == "4":
            mid = input("Member ID: ")
            bid = input("Book ID: ")
            library.return_book(mid, bid)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            library.display_members()

        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()
