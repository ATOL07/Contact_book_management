import add_contact
import load_save
import display_contacts

contacts = load_save.load_contacts()  # Load contacts from file

while True:
    print("\nWelcome to Contact Book Management System")
    print("0. Exit")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Update Contacts")
    print("4. Search Contacts")
    print("5. Remove Contacts")

    menu = input("Select an option: ").strip()

    if menu == "0":
        load_save.save_contacts(contacts)  # Save contacts to file before exiting
        print("Contacts saved to successfully Goodbye!")
        break
    elif menu == "1":
        contacts = add_contact.add_contact(contacts)
        load_save.save_contacts(contacts)  # Save after adding a new contact
    elif menu == "2":
        load_save.display_contacts(contacts=display_contacts)  # Display all contacts
    else:
        print("Invalid option, please try again.")
