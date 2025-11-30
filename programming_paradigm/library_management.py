class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
    
    class library:
        def __init__(self):
            self.__books = []

        def add_book(self, book):
            self.__books.append(book)

        def check_out_book(self, title):
            for book in self.__books:
                if book.title.lower() == title.lower():
                    if book.check_out():
                        return f"'{title}' checked out successfully."
                    else:
                        return f"Book titled '{title}' is already checked out."
            return f"Book titled '{title}' not found."
        
        def return_book(self, title):
            for book in self.__books:
                if book.title.lower() == title.lower():
                    if book.return_book():
                        return f"'{title}' returned successfully."
                    else:
                        return f"'{title}' was not checked out."
            return f"Book titled '{title}' not found."
        
        def list_available_books(self):
            available = [book.title for book in self.__books if book.is_available()]
            return available if available else ["No available books"]
                    