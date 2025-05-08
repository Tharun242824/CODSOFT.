import tkinter as tk
from tkinter import messagebox, simpledialog

# List to store contacts
contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()
    
    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    update_contact_list()
    clear_fields()

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = search_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact["name"].lower() or query in contact["phone"]:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        del contacts[selected_index]
        update_contact_list()
        clear_fields()
    except IndexError:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")

def select_contact(event):
    try:
        index = contact_listbox.curselection()[0]
        contact = contacts[index]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])
    except IndexError:
        pass

def update_contact():
    try:
        selected_index = contact_listbox.curselection()[0]
        contacts[selected_index] = {
            "name": name_entry.get().strip(),
            "phone": phone_entry.get().strip(),
            "email": email_entry.get().strip(),
            "address": address_entry.get().strip()
        }
        update_contact_list()
        clear_fields()
    except IndexError:
        messagebox.showwarning("Select Contact", "Select a contact to update.")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x550")

# Input Fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

# Search Box
tk.Label(root, text="Search by Name or Phone").pack()
search_entry = tk.Entry(root)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

# Contact List
contact_listbox = tk.Listbox(root, width=50)
contact_listbox.pack(pady=10)
contact_listbox.bind("<<ListboxSelect>>", select_contact)

# Run
root.mainloop()
