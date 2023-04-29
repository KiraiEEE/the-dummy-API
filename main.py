import tkinter as tk
import os

window = tk.Tk()
window.title("Books Manager v0.1")
window.geometry("600x450")
window.config(bg="#0E0F11")

logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img.png")
logo_image = tk.PhotoImage(file=logo_path)
logo_label = tk.Label(image=logo_image, bg="#0E0F11")
search_button = tk.Button(text="SEARCH", width=20, height=2, bg="#0077be", fg="white")
insert_button = tk.Button(text="INSERT", width=20, height=2, bg="#0077be", fg="white")
update_button = tk.Button(text="UPDATE", width=20, height=2, bg="#0077be", fg="white")
remove_button = tk.Button(text="REMOVE", width=20, height=2, bg="#0077be", fg="white")

logo_label.pack(side=tk.TOP, pady=10)
search_button.pack(pady=10)
insert_button.pack(pady=10)
update_button.pack(pady=10)
remove_button.pack(pady=10)

def search_books():
    os.system("python get_gui.py")

def insert_book():
    os.system("python post_gui.py")

def update_book():
    os.system("python put_gui.py")

def remove_book():
    os.system("python delete_gui.py")

search_button.config(command=search_books)
insert_button.config(command=insert_book)
update_button.config(command=update_book)
remove_button.config(command=remove_book)

window.mainloop()
