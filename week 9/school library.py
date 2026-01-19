
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN    

    def display(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}'


class DetailedBook(Book):
    def __init__(self, title, author, ISBN, genre, length):
        super().__init__(title, author, ISBN)
        self.genre = genre
        self.length = length

    def display(self):
        return (f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, '
                f'Genre: {self.genre}, Length: {self.length} pages')


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' has been removed from the library.")
        else:
            print(f"Book '{book.title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(" -", book.display())

    def search_by_title(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print("Book found:", book.display())
                found = True
        if not found:
            print(f"No book found with title containing '{title}'.")


book1 = DetailedBook("Deep Sea", "George W.", "978-3-16-148410-0", "Mystery", 250)
book2 = DetailedBook("High Waves", "Martin V.", "978-4-16-142210-1", "Fantasy", 300)
book3 = DetailedBook("High Castle", "David D.", "978-6-28-258410-4", "Drama", 400)

my_library = Library()
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.list_books()
my_library.search_by_title("High Waves")
my_library.remove_book(book2)
my_library.list_books()
