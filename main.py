import json
import os

FILENAME = "contacts.json"



#Function to load contacts at startup
def load_contacts():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, "r") as f:
        return json.load(f)

#Function to save contacts to file at exit
def save_contacts(contacts):

    print(contacts)
    
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

#Function to update contact list
def add_contact(contacts):

    print(contacts)
    
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully.")

#Function to view contacts list
def view_contacts(contacts):
    
    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

#Function to search for contacts in list
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").strip().lower()

    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
            found = True

    if not found:
        print("No matching contact found.")

#Function to delete contacts from list
def delete_contact(contacts):
    view_contacts(contacts)

    try:
        index = int(input("Enter contact number to delete: "))
        removed = contacts.pop(index - 1)
        print(f"Deleted: {removed['name']}")
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():

    #Load contacts list at startup
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
