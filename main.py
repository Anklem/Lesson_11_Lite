from library_manager.catalog import Book, Library
from library_manager.report import generate_report

book1 = Book("Идиот", "Достоевский", "драма")
book2 = Book("100 лет одиночества", "Маркес", "фэнтези")
book3 = Book("Война и мир", "Толстой", "эпопея")
book4 = Book("Мы", "Замятин", "антиутопия")

book5 = Book("1984", "Orwell", None)

library = Library()

try:
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
except ValueError:
    print("Ошибка при регистрации книги")

print(generate_report(library))

print("Удаляем 'Войну и мир'")
library.remove_book("Война и мир")

print(generate_report(library))

print("Ищем 'Мы'")
found_books = library.search_book("Мы", "Замятин", "антиутопия")
print(found_books[0])