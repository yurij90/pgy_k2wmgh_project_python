def PG_load_books():
    return ["Python alapok", "Java bevezetés", "Algoritmusok"]

def PG_add_book(title, book_list):
    book_list.append(title)
    return book_list

def PG_remove_book(title, book_list):
    if title in book_list:
        book_list.remove(title)
    return book_list