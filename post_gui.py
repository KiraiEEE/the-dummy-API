import tkinter as tk
import requests
from tkinter import messagebox


class AddBookGUI:
    def __init__(self, master):
        self.master = master
        master.title("Add Book")
        
        self.author_label = tk.Label(master, text="Author:")
        self.author_label.pack()
        self.author_entry = tk.Entry(master)
        self.author_entry.pack()
        
        self.title_label = tk.Label(master, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(master)
        self.title_entry.pack()
        
        self.country_label = tk.Label(master, text="Country:")
        self.country_label.pack()
        self.country_entry = tk.Entry(master)
        self.country_entry.pack()
        
        self.language_label = tk.Label(master, text="Language:")
        self.language_label.pack()
        self.language_entry = tk.Entry(master)
        self.language_entry.pack()
        
        self.pages_label = tk.Label(master, text="Pages:")
        self.pages_label.pack()
        self.pages_entry = tk.Entry(master)
        self.pages_entry.pack()
        
        self.year_label = tk.Label(master, text="Year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(master)
        self.year_entry.pack()
        
        self.link_label = tk.Label(master, text="Link:")
        self.link_label.pack()
        self.link_entry = tk.Entry(master)
        self.link_entry.pack()
        
        self.image_label = tk.Label(master, text="Image Link:")
        self.image_label.pack()
        self.image_entry = tk.Entry(master)
        self.image_entry.pack()
        
        self.add_button = tk.Button(master, text="Add Book", command=self.add_book)
        self.add_button.pack()

    def add_book(self):
        new_book = {
            "author": self.author_entry.get(),
            "country": self.country_entry.get(),
            "imageLink": self.image_entry.get(),
            "language": self.language_entry.get(),
            "link": self.link_entry.get(),
            "pages": self.pages_entry.get(),
            "title": self.title_entry.get(),
            "year": self.year_entry.get()
        }

        response = requests.post('http://localhost:5000/books', json=new_book)

        if response.status_code == 201:
            new_book = response.json()

            message = f"New book added: {new_book['title']} ({new_book['year']})"
            messagebox.showinfo("Success", message)
            
            self.author_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.country_entry.delete(0, tk.END)
            self.language_entry.delete(0, tk.END)
            self.pages_entry.delete(0, tk.END)
            self.year_entry.delete(0, tk.END)
            self.link_entry.delete(0, tk.END)
            self.image_entry.delete(0, tk.END)
        else:
            message = f"An error occurred: {response.status_code}"
            messagebox.showinfo("Error", message)

root = tk.Tk()
root.geometry("400x400")
add_book_gui = AddBookGUI(root)
root.mainloop()
