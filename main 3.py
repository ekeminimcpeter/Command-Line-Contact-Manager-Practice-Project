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
    
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)

#Function to update contact list
def add_contact(contacts):
    
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
    
    #Update contact list ID (index/counter) and contact and print ID-tagged Item list.
    
    for i, contact in enumerate(contacts, start=1):  # start counter variable at 1.
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

#Function to search for contacts in list
def search_contact(contacts):
    keyword = input("Enter name or phone to search: ").strip().lower() # remove leading and trailing whitespaces and normalise string to lowercase.

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
    contacts = load_contacts()
    saved = True   # flag to track if data is changed and saved. Initially, loaded data is considered saved

    while True:
        
        print("\n--- Contact Manager ---")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip() # remove leading and trailing whitespaces 

        if choice == "1":
            
            add_contact(contacts)
            saved = False # mark data as unsaved when modified
                
        elif choice == "2": 
            view_contacts(contacts) #viewing does not change data
                
        elif choice == "3":
            search_contact(contacts) # viewing does not change data
                
        elif choice == "4":
            delete_contact(contacts)
            saved = False # mark data as unsaved when modified

        elif choice == "5":
            
            if not saved and contacts: # if the file is not saved AND there is actually data in the list, then do something.
                while True:
                    print("\nYour contact is not saved.")
                    print("Do you want to end the program without saving?")
                    print("1. Save and exit")
                    print("2. Exit without saving")
                    print("3. Cancel")

                    confirm = input("Enter 1 or 2 or 3 (or yes/no/cancel): ").strip().lower() # get user confirmation input.

                    if confirm in ("1", "yes"):
                        save_contacts(contacts)
                        print("Contacts saved. Goodbye.")
                        return   # leave main() cleanly

                    elif confirm in ("2", "no"):
                        print("Exiting without saving. Goodbye.")
                        return   # leave main() cleanly

                    elif confirm in ("3", "cancel"):
                        print("Exit cancelled. Returning to menu.")
                        break  # break only inner loop → go back to menu

                    else:
                        print("Invalid choice. Please enter 1 or 2 or 3, yes or no or cancel.")

        else:
            # Nothing changed or nothing to save
            print("Goodbye.")
            
if __name__ == "__main__":
    main()


            
