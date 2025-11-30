import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()



from library_management import Book, Library
library = Library()

library.add_book(Book("Atomic Habits", "James Clear"))
library.add_bbok(Book("Python Crash Coarse", "Eric Matthes"))
library.add_book(Book("The alchemist", "Paulo Coelho"))

print(library.check_out_book("Atomic Habits"))
print("Available books:", library.list_available_books())
print(library.return_book("Atomic Habits"))
print("Available books:", library.list_available_books())
