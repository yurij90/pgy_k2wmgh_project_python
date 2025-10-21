import tkinter as tk
from tkinter import messagebox
from book_PG import PG_add_book, PG_remove_book, PG_load_books

class App_PG:
    def __init__(self, root):
        self.root = root
        self.root.title("Könyvkezelő PG")
        self.root.geometry("400x400")

        self.books = PG_load_books()

        self.input_var = tk.StringVar()

        self.entry = tk.Entry(root, textvariable=self.input_var)
        self.entry.pack(pady=5)
        self.entry.bind('<Return>', lambda event: self.add_book())

        self.add_button = tk.Button(root, text="Hozzáadás", command=self.add_book)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Törlés", command=self.remove_book)
        self.remove_button.pack(pady=5)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10)
        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for b in self.books:
            self.listbox.insert(tk.END, b)

    def add_book(self):
        title = self.input_var.get().strip()
        if title:
            if title in self.books:
                messagebox.showwarning("Figyelem", "Ez a könyv már szerepel a listában!")
            else:
                self.books = PG_add_book(title, self.books)
                self.refresh_list()
                self.input_var.set("")
        else:
            messagebox.showwarning("Figyelem", "Nem adhatod hozzá az üres könyvcímet!")

    def remove_book(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            selected = self.listbox.get(selected_indices[0])
            self.books = PG_remove_book(selected, self.books)
            self.refresh_list()
        else:
            messagebox.showwarning("Figyelem", "Válassz egy könyvet a törléshez!")
