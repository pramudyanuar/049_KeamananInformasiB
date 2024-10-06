import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import random
import string


#tkinter setup
T = tk.Tk()
T.geometry("600x400")
T.title("DEScryptor!")
T.configure(background="#1e1e1e")

button_style = {
    "font": ("Arial", 12, "bold"),
    "fg": "white",
    "bg": "#6e6e6e",
    "activebackground": "#4a4a4a",
    "bd": 0,
    "relief": "flat",
    "width": 10
}
label_style = {
    "font": ("Arial", 10, "bold"),
    "fg": "white",
    "bg": "#1e1e1e"
}
text_area_style = {
    "font": ("Arial", 12),
    "bg": "#dcdcdc",
    "height": 5,
    "width": 20,
    "bd": 0,
    "padx": 10,
    "pady": 10
}


def Encrypt():
   pass

def Decrypt():
    pass

def update_mode(mode):
    final_encrypt_btn.config(text=mode)

def clear1():
    plain_text.delete(1.0, tk.END)

def clear2():
    cipher_text.delete(1.0, tk.END)

def generate_random_key():
    random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    key_entry.delete(0, tk.END)
    key_entry.insert(0, random_key)

def encrypt_text():
    key = key_entry.get()
    text = plain_text.get(1.0, tk.END).strip()
    if not key or not text:
        messagebox.showerror("Input Error", "Please provide both key and plain text.")
        return
    if len(key) != 8:
        messagebox.showerror("Key Error", "Key must be 8 characters long (64-bit DES key).")
        return
    try:
        pass
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def decrypt_text():
    key = key_entry.get()
    text = cipher_text.get(1.0, tk.END).strip()
    if not key or not text:
        messagebox.showerror("Input Error", "Please provide both key and cipher text.")
        return
    if len(key) != 8:
        messagebox.showerror("Key Error", "Key must be 8 characters long (64-bit DES key).")
        return
    try:
        pass
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

def handle_final_button_click():
    mode = final_encrypt_btn.cget("text")
    if mode == "Encrypt":
        encrypt_text()
    elif mode == "Decrypt":
        decrypt_text()
        
final_encrypt_btn = tk.Button(T, text="Encrypt", **button_style, command=handle_final_button_click)
final_encrypt_btn.place(x=260, y=320)

key_label = tk.Label(T, text="Key", **label_style)
key_label.place(x=140, y=50)
key_entry = tk.Entry(T, font=("Arial", 12), width=25)
key_entry.place(x=140, y=80)

random_btn = tk.Button(T, text="Random", **button_style, command=generate_random_key)
random_btn.place(x=400, y=77)

encrypt_btn = tk.Button(T, text="Encrypt", **button_style, command=lambda: update_mode("Encrypt"))
encrypt_btn.place(x=20, y=50)

decrypt_btn = tk.Button(T, text="Decrypt", **button_style, command=lambda: update_mode("Decrypt"))
decrypt_btn.place(x=20, y=100)

plain_text_label = tk.Label(T, text="Plain Text", **label_style)
plain_text_label.place(x=140, y=150)
plain_text = ScrolledText(T, **text_area_style)
plain_text.place(x=140, y=180)

cipher_text_label = tk.Label(T, text="Cipher Text", **label_style)
cipher_text_label.place(x=380, y=150)
cipher_text = ScrolledText(T, **text_area_style)
cipher_text.place(x=380, y=180)

title_label = tk.Label(T, text="DEScryptor!", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
title_label.place(x=280, y=20)


T.mainloop()
