import requests
import tkinter as tk
from tkinter import messagebox


def update_book():

    book_name = entry_book_name.get()


    updated_book = {}


    if entry_author.get():
        updated_book["author"] = entry_author.get()
    if entry_country.get():
        updated_book["country"] = entry_country.get()
    if entry_image_link.get():
        updated_book["imageLink"] = entry_image_link.get()
    if entry_language.get():
        updated_book["language"] = entry_language.get()
    if entry_link.get():
        updated_book["link"] = entry_link.get()
    if entry_pages.get():
        updated_book["pages"] = entry_pages.get()
    if entry_title.get():
        updated_book["title"] = entry_title.get()
    if entry_year.get():
        updated_book["year"] = entry_year.get()


    response = requests.put(f'http://localhost:5000/books/{book_name}', json=updated_book)


    if response.status_code == 200:
        updated_book = response.json()
        message = f"Book updated: {updated_book['title']} ({updated_book['year']})"
        tk.messagebox.showinfo("Success", message)
    else:
        message = f"An error occurred: {response.status_code}"
        tk.messagebox.showerror("Error", message)

window = tk.Tk()
window.title("Update Book")
window.geometry("230x300")

tk.Label(window, text="Book to update").grid(row=0, column=0)
entry_book_name = tk.Entry(window)
entry_book_name.grid(row=0, column=1,pady=30)

tk.Label(window, text="Author").grid(row=1, column=0)
entry_author = tk.Entry(window)
entry_author.grid(row=1, column=1)

tk.Label(window, text="Country").grid(row=2, column=0)
entry_country = tk.Entry(window)
entry_country.grid(row=2, column=1)

tk.Label(window, text="Image Link").grid(row=3, column=0)
entry_image_link = tk.Entry(window)
entry_image_link.grid(row=3, column=1)

tk.Label(window, text="Language").grid(row=4, column=0)
entry_language = tk.Entry(window)
entry_language.grid(row=4, column=1)

tk.Label(window, text="Link").grid(row=5, column=0)
entry_link = tk.Entry(window)
entry_link.grid(row=5, column=1)

tk.Label(window, text="Pages").grid(row=6, column=0)
entry_pages = tk.Entry(window)
entry_pages.grid(row=6, column=1)

tk.Label(window, text="Title").grid(row=7, column=0)
entry_title = tk.Entry(window)
entry_title.grid(row=7, column=1)

tk.Label(window, text="Year").grid(row=8, column=0)
entry_year = tk.Entry(window)
entry_year.grid(row=8, column=1)

btn_update = tk.Button(window, text="Update", command=update_book)
btn_update.grid(row=9, column=0, columnspan=2)
window.mainloop()
