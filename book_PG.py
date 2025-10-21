import os
from class_PG import Book_PG

FILE_NAME = "books.txt"

def PG_load_books():
    books = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(";")
                    title = parts[0]
                    author = parts[1] if len(parts) > 1 else "Ismeretlen szerző"
                    books.append(Book_PG(title, author))
    if not books:
        books = [
            Book_PG("Python alapjai", "Nagy Péter"),
            Book_PG("Java bevezető", "Kovács Ádám"),
            Book_PG("Algoritmusok alapjai", "Szabó Tamás")
        ]
        PG_save_books(books)
    return books

def PG_save_books(book_list):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for book in book_list:
            f.write(f"{book.title};{book.author}\n")

def PG_add_book(book, book_list):
    book_list.append(book)
    PG_save_books(book_list)
    return book_list

def PG_remove_book(book, book_list):
    if book in book_list:
        book_list.remove(book)
        PG_save_books(book_list)
    return book_list
