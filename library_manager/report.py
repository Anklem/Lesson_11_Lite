# Генерирует отчет о всех книгах в библиотеке в формате строки
from library_manager.catalog import Library
from library_manager.utils.formatting import format_book_data

def generate_report(library: Library):

    report = "\nБиблиотека:\n"
    for book in library.get_all_books():
        report += format_book_data(book) + "\n"

    return report
