import tkinter as tk
import requests
import io
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Books by Author")
window.geometry("600x400")

author_label = tk.Label(text="Enter Author Name:")
author_entry = tk.Entry()
search_button = tk.Button(text="Search")

books_listbox = tk.Listbox(width=50)
book_title_label = tk.Label(text="")
book_author_label = tk.Label(text="")
book_year_label = tk.Label(text="")
book_country_label = tk.Label(text="")
book_language_label = tk.Label(text="")
book_pages_label = tk.Label(text="")
book_image_label = tk.Label()

author_label.pack()
author_entry.pack()
search_button.pack()
books_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
book_title_label.pack()
book_author_label.pack()
book_year_label.pack()
book_country_label.pack()
book_language_label.pack()
book_pages_label.pack()
book_image_label.pack()

def on_book_select(event):
    selected_book = books_listbox.get(books_listbox.curselection())
    for book in books:
        if book['title'] == selected_book:
            book_title_label.config(text=f"Title: {book['title']}")
            book_author_label.config(text=f"Author: {book['author']}")
            book_year_label.config(text=f"Year: {book['year']}")
            book_country_label.config(text=f"Country: {book['country']}")
            book_language_label.config(text=f"Language: {book['language']}")
            book_pages_label.config(text=f"Pages: {book['pages']}")
            response = requests.get(book['imageLink'])
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
            book_image_label.config(image=img)
            book_image_label.image = img 

def search_books():
    author_name = author_entry.get()
    response = requests.get('http://localhost:5000/books', params={'author': author_name})
    if response.status_code == 200:
        global books
        books = response.json()
        books_listbox.delete(0, tk.END)
        for book in books:
            books_listbox.insert(tk.END, book['title'])
    else:
        books_listbox.delete(0, tk.END)
        book_title_label.config(text="")
        book_author_label.config(text="")
        book_year_label.config(text="")
        book_country_label.config(text="")
        book_language_label.config(text="")
        book_pages_label.config(text="")
        book_image_label.config(image=None)
        print(f"An error occurred: {response.status_code}")

search_button.config(command=search_books)

books_listbox.bind('<<ListboxSelect>>', on_book_select)
window.mainloop()

