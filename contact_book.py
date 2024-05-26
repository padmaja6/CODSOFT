
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contact List:")
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone_number']}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone_number']:
                found_contacts.append(contact)
        if not found_contacts:
            print("No matching contacts found.")
            return
        print("Matching Contacts:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone_number']}")

    def update_contact(self, index, new_data):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return
        self.contacts[index - 1].update(new_data)
        print("Contact updated successfully!")

    def delete_contact(self, index):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact index.")
            return
        del self.contacts[index - 1]
        print("Contact deleted successfully!")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone_number, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)

        elif choice == '4':
            index = int(input("Enter index of contact to update: "))
            new_data = {
                'name': input("Enter new name: "),
                'phone_number': input("Enter new phone number: "),
                'email': input("Enter new email: "),
                'address': input("Enter new address: ")
            }
            manager.update_contact(index, new_data)

        elif choice == '5':
            index = int(input("Enter index of contact to delete: "))
            manager.delete_contact(index)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
