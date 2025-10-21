from class_PG import Book_PG

def PG_load_books():
    return [
        Book_PG("Python alapok", "Szerző A"),
        Book_PG("Java bevezetés", "Szerző B"),
        Book_PG("Algoritmusok", "Szerző C")
    ]

def PG_add_book(book, book_list):
    book_list.append(book)
    return book_list

def PG_remove_book(book, book_list):
    if book in book_list:
        book_list.remove(book)
    return book_list
