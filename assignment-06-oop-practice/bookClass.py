class Book:
    total_books = 0
    def __init__ (self):
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        print(f"total books {cls.total_books}")

book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()
Book.increment_book_count()