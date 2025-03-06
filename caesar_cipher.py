import tkinter as tk
from tkinter import ttk, messagebox

# Caesar Cipher Functions
def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char
    return result

def encrypt_message():
    shift = shift_entry.get()
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number")
        return
    shift = int(shift)
    message = message_entry.get()
    encrypted_text = caesar_cipher(message, shift, encrypt=True)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Encrypted: {encrypted_text}\n")
    chat_display.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

def decrypt_message():
    shift = shift_entry.get()
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be a number")
        return
    shift = int(shift)
    message = message_entry.get()
    decrypted_text = caesar_cipher(message, shift, encrypt=False)
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Decrypted: {decrypted_text}\n")
    chat_display.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

def save_message():
    message = chat_display.get("1.0", tk.END).strip()
    if message:
        saved_messages.insert(tk.END, message)

def delete_selected():
    selected = saved_messages.curselection()
    for index in selected[::-1]:
        saved_messages.delete(index)

def new_chat():
    chat_display.config(state=tk.NORMAL)
    chat_display.delete("1.0", tk.END)
    chat_display.config(state=tk.DISABLED)

# Initialize Main Window
root = tk.Tk()
root.title("Chat Application")
root.geometry("900x550")
root.configure(bg="#2C2F33")

# Sidebar (20%)
sidebar = tk.Frame(root, bg="#1E1E1E", width=180)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Dark Mode Toggle Button
dark_mode_btn = tk.Button(sidebar, text="🌙", bg="#3C3F41", fg="white", relief=tk.FLAT)
dark_mode_btn.pack(pady=10, padx=5)

# Chat Header (Fixed)
header = tk.Frame(root, bg="#000000", height=50)
header.pack(fill=tk.X)
chat_label = tk.Label(header, text="R&S Developers", bg="#000000", fg="white", font=("Arial", 12, "bold"))
chat_label.pack(side=tk.LEFT, padx=10)

# New Chat & Save Buttons
new_chat_btn = tk.Button(header, text="New Chat", bg="#2196F3", fg="white", relief=tk.FLAT, command=new_chat)
save_btn = tk.Button(header, text="Save", bg="#FF9800", fg="black", relief=tk.FLAT, command=save_message)
new_chat_btn.pack(side=tk.RIGHT, padx=5, pady=5)
save_btn.pack(side=tk.RIGHT, padx=5, pady=5)

# Chat Display (Scrollable)
chat_frame = tk.Frame(root, bg="#2C2F33")
chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
chat_display = tk.Text(chat_frame, bg="#2C2F33", fg="white", font=("Arial", 12), state=tk.DISABLED)
chat_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
chat_scroll = tk.Scrollbar(chat_frame, command=chat_display.yview)
chat_scroll.pack(side=tk.RIGHT, fill=tk.Y)
chat_display.config(yscrollcommand=chat_scroll.set)

# Message Entry Box & Shift Input
entry_frame = tk.Frame(root, bg="#2C2F33")
entry_frame.pack(fill=tk.X, padx=10, pady=5)
shift_entry = tk.Entry(entry_frame, bg="#3C3F41", fg="white", font=("Arial", 12), width=5)
message_entry = tk.Entry(entry_frame, bg="#3C3F41", fg="white", font=("Arial", 12), width=50)
shift_entry.pack(side=tk.LEFT, padx=5, pady=5)
message_entry.pack(side=tk.LEFT, padx=10, pady=5, fill=tk.X, expand=True)

# Encrypt & Decrypt Buttons
encrypt_btn = tk.Button(entry_frame, text="Encrypt", bg="#4CAF50", fg="white", relief=tk.FLAT, command=encrypt_message)
decrypt_btn = tk.Button(entry_frame, text="Decrypt", bg="#E91E63", fg="white", relief=tk.FLAT, command=decrypt_message)
encrypt_btn.pack(side=tk.RIGHT, padx=5)
decrypt_btn.pack(side=tk.RIGHT, padx=5)

# Sidebar Saved Messages (Scrollable)
saved_messages = tk.Listbox(sidebar, bg="#3C3F41", fg="white")
saved_messages.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Select & Delete Buttons
bottom_buttons = tk.Frame(sidebar, bg="#1E1E1E")
bottom_buttons.pack(fill=tk.X)
select_btn = tk.Button(bottom_buttons, text="Select", bg="#3C3F41", fg="white")
delete_btn = tk.Button(bottom_buttons, text="Delete", bg="red", fg="white", command=delete_selected)
select_btn.pack(side=tk.LEFT, padx=5, pady=5)
delete_btn.pack(side=tk.RIGHT, padx=5, pady=5)

root.mainloop()