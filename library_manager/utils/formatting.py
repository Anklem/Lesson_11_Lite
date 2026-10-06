from library_manager.catalog import Book


def format_book_data(book: Book) -> str:
    return f"Title: {book.title}, Author: {book.author}, Genre: {book.genre}"
