contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {details['phone_number']}")
        print(f"  Email: {details['email']}")
        print(f"  Address: {details['address']}")
        print()

def search_contact():
    search_term = input("Enter name or phone number to search: ").strip()
    
    results = {name: details for name, details in contacts.items() if search_term in name or search_term in details['phone_number']}
    
    if not results:
        print("No matching contacts found.")
        return
    
    print("\nSearch Results:")
    for name, details in results.items():
        print(f"Name: {name}")
        print(f"  Phone: {details['phone_number']}")
        print(f"  Email: {details['email']}")
        print(f"  Address: {details['address']}")
        print()

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()
    
    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return
    
    print(f"Updating contact '{name}':")
    phone_number = input(f"Enter new phone number (current: {contacts[name]['phone_number']}): ") or contacts[name]['phone_number']
    email = input(f"Enter new email address (current: {contacts[name]['email']}): ") or contacts[name]['email']
    address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]['address']
    
    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    
    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return
    
    del contacts[name]
    print(f"Contact '{name}' deleted successfully!")

def main_menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
