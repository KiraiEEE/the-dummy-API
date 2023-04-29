import tkinter as tk
import os
window = tk.Tk()
window.title("Library Management System v0.1")
window.geometry("500x510")

logo = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(image=logo)
search_button = tk.Button(text="SEARCH", font=("Arial", 20), width=12, command=lambda: os.system('python get_gui.py'))
insert_button = tk.Button(text="INSERT", font=("Arial", 20), width=12, command=lambda: os.system('python post_gui.py'))
update_button = tk.Button(text="UPDATE", font=("Arial", 20), width=12, command=lambda: os.system('python put_gui.py'))
remove_button = tk.Button(text="REMOVE", font=("Arial", 20), width=12, command=lambda: os.system('python delete_gui.py'))

logo_label.pack()
search_button.pack(pady=(20, 10))
insert_button.pack(pady=10)
update_button.pack(pady=10)
remove_button.pack(pady=10)

window.mainloop()
