class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No contacts found.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, contact_index, new_contact):
        self.contacts[contact_index] = new_contact

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]

def main():
    contact_book = ContactBook()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully!")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Found Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contacts found.")
        elif choice == '4':
            contact_book.view_contacts()
            try:
                contact_index = int(input("Enter index of contact to update: ")) - 1
                name = input("Enter new name: ")
                phone = input("Enter new phone number: ")
                email = input("Enter new email address: ")
                address = input("Enter new address: ")
                updated_contact = Contact(name, phone, email, address)
                contact_book.update_contact(contact_index, updated_contact)
                print("Contact updated successfully!")
            except (IndexError, ValueError):
                print("Invalid input. Please enter a valid contact index.")
        elif choice == '5':
            contact_book.view_contacts()
            try:
                contact_index = int(input("Enter index of contact to delete: ")) - 1
                contact_book.delete_contact(contact_index)
                print("Contact deleted successfully!")
            except (IndexError, ValueError):
                print("Invalid input. Please enter a valid contact index.")
        elif choice == '6':
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
