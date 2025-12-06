class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
    def __repr__(self):
        return f"Book '{self.title}', '{self.author}'"
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB)"
    
    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count})"
    
    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book}")
        else:
            print(f"Error: {book} is not a valid Book instance.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        print(f"\n{'=' * 60}")
        print(f"Library Collection ({len(self.books)} book(s)):")
        print(f"{'=' * 60}")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print(f"{'=' * 60}\n")

    def __len__(self):
        return len(self.books)
    
    def __str__(self):
        return f"Library with {len(self.books)} book(s)"
    
    def __repr__(self):
        return f"Library(books = {len(self.books)})"