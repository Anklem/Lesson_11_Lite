from library_manager.catalog import Book


def validate_book_data(book) -> bool:

    if not isinstance(book, Book): return False

    return book.title is not None and book.genre is not None and book.author is not None