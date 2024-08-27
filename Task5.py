# Task - 5

# Contact Information: Store name, phone number, email, and address for each contact.

# Add Contact: Allow users to add new contacts with their details.
# View Contact List: Display a list of all saved contacts with names and phone numbers.

# Search Contact: Implement a search function to find contacts by name or phone number.
# Update Contact: Enable users to update contact details.

# Delete Contact: Provide an option to delete a contact.
# User Interface: Design a user-friendly interface for easy interaction.

import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"

class ContactManager:
    def __init__(self, root):
        self.contacts = []
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("600x400")

        
        self.search_var = tk.StringVar()
        tk.Label(root, text="Search:").grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=30)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)
        self.search_entry.bind('<KeyRelease>', self.filter_contacts)

        
        self.listbox_frame = tk.Frame(root)
        self.listbox_frame.grid(row=1, column=0, padx=10, pady=10, rowspan=6)

        self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")
        self.listbox = tk.Listbox(self.listbox_frame, height=15, width=30, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left", fill="both", expand=True)

        self.listbox.bind('<<ListboxSelect>>', self.display_contact_details)

        
        self.detail_frame = tk.Frame(root)
        self.detail_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

        tk.Label(self.detail_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(self.detail_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.detail_frame, text="Phone:").grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(self.detail_frame)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.detail_frame, text="Email:").grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(self.detail_frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.detail_frame, text="Address:").grid(row=3, column=0, sticky="e")
        self.address_entry = tk.Entry(self.detail_frame)
        self.address_entry.grid(row=3, column=1)

        
        self.add_button = tk.Button(self.detail_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, pady=5)

        self.update_button = tk.Button(self.detail_frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1, pady=5)

        self.delete_button = tk.Button(self.detail_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=7, column=1, pady=10)

    def refresh_listbox(self, contacts=None):
        self.listbox.delete(0, tk.END)
        contacts = contacts if contacts is not None else self.contacts
        for contact in contacts:
            self.listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append(Contact(name, phone, email, address))
            self.refresh_listbox()
            self.clear_details()
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required fields.")

    def update_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            contact.name = self.name_entry.get()
            contact.phone = self.phone_entry.get()
            contact.email = self.email_entry.get()
            contact.address = self.address_entry.get()
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
            if confirm:
                del self.contacts[selected_index[0]]
                self.refresh_listbox()
                self.clear_details()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def display_contact_details(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact.name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact.phone)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact.email)
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, contact.address)

    def filter_contacts(self, event):
        search_term = self.search_var.get().lower()
        filtered_contacts = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]
        self.refresh_listbox(filtered_contacts)

    def clear_details(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
