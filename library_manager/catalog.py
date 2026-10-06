from library_manager.book import Book
from library_manager.utils.data_validation import validate_book_data


class Library:

    def __init__(self):
        self.books = []

    def __str__(self):
        return self.books

    def add_book(self, book: Book):
        if validate_book_data(book):
            self.books.append(book)
        else:
            raise ValueError("Invalid book data")

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def search_book(self, title, author, genre):
        return [book for book in self.books if book.title == title and book.author == author and book.genre == genre]

    def get_all_books(self):
        return self.books
