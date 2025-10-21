import tkinter as tk
from tkinter import messagebox
from book_PG import PG_add_book, PG_remove_book, PG_load_books
from class_PG import Book_PG

class App_PG:
    def __init__(self, root):
        self.root = root
        self.root.title("Könyvkezelő PG")
        self.root.geometry("350x450")

        self.books = PG_load_books()

        tk.Label(root, text="Könyv címe:").pack(pady=(10, 0), padx=10, anchor='w')
        self.title_var = tk.StringVar()
        self.entry_title = tk.Entry(root, textvariable=self.title_var)
        self.entry_title.pack(pady=5, padx=10, fill='x')
        self.entry_title.bind('<Return>', self.on_title_enter)

        tk.Label(root, text="Szerző:").pack(pady=(10, 0), padx=10, anchor='w')
        self.author_var = tk.StringVar()
        self.entry_author = tk.Entry(root, textvariable=self.author_var)
        self.entry_author.pack(pady=5, padx=10, fill='x')
        self.entry_author.bind('<Return>', lambda event: self.add_book())

        self.add_button = tk.Button(root, text="Hozzáadás", command=self.add_book_or_focus_author)
        self.add_button.pack(pady=(10, 5))

        self.remove_button = tk.Button(root, text="Törlés", command=self.remove_book)
        self.remove_button.pack(pady=5)

        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, fill='both', expand=True, padx=5)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side='right', fill='y', padx=(0,2))

        self.listbox = tk.Listbox(list_frame, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side='left', fill='both', expand=True, padx=(0,2))

        self.scrollbar.config(command=self.listbox.yview)

        self.refresh_list()

    def on_title_enter(self, event):
        if not self.author_var.get().strip():
            self.entry_author.focus_set()
        else:
            self.add_book()

    def add_book_or_focus_author(self):
        if not self.author_var.get().strip():
            self.entry_author.focus_set()
        else:
            self.add_book()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for book in self.books:
            self.listbox.insert(tk.END, book.get_info())

    def add_book(self):
        title = self.title_var.get().strip()
        author = self.author_var.get().strip()
        if not title:
            messagebox.showwarning("Figyelem", "Nem adhatod hozzá az üres könyvcímet!")
            return
        if not author:
            author = "Ismeretlen szerző"
        if any(book.title == title for book in self.books):
            messagebox.showwarning("Figyelem", "Ez a könyv már szerepel a listában!")
            return

        new_book = Book_PG(title, author)
        self.books = PG_add_book(new_book, self.books)
        self.refresh_list()
        self.title_var.set("")
        self.author_var.set("")

    def remove_book(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            idx = selected_indices[0]
            book = self.books[idx]
            self.books = PG_remove_book(book, self.books)
            self.refresh_list()
        else:
            messagebox.showwarning("Figyelem", "Válassz egy könyvet a törléshez!")
