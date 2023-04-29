import tkinter as tk
import requests
from tkinter import messagebox

def delete_book_by_name():
    book_name = book_name_entry.get()
    response = requests.delete(f'http://localhost:5000/books?name={book_name}')
    if response.status_code == 200:
        deleted_book = response.json()
        message = f'Successfully deleted book: {deleted_book["title"]}'
    elif response.status_code == 404:
        message = f'Book not found: {book_name}'
    else:
        message = f'Error deleting book: {response.status_code}'
    messagebox.showinfo("Delete Book", message)

window = tk.Tk()
window.geometry("200x200")
window.title("Delete Book")

book_name_label = tk.Label(window, text="Book Name:")
book_name_label.pack()

book_name_entry = tk.Entry(window)
book_name_entry.pack()

delete_button = tk.Button(window, text="Delete Book", command=delete_book_by_name)
delete_button.pack()

window.mainloop()
