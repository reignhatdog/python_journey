#Contact Book

contacts = {}

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Added contact: {name}")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
    else:
        print("Contacts")
        for name, info in contacts.items():
            print(f"{name} - {info['phone']} - {info['email']}")

def remove_contact():
    name = input("Enter name to remove: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Removed contact: {name}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("Day 10: Contact Book")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Remove contact")
        print("4. Exit")

        choice = input("Choose (1-4): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            remove_contact()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
