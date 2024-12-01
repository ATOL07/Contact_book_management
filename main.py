import add_contact
import load_save
import search_contact
import update_contact
import remove_contact

contacts = load_save.load_contacts()  # Loading contacts from file

while True:
    print("\nWelcome to Contact Book Management System")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Update Contacts")
    print("4. Search Contacts")
    print("5. Remove Contacts")
    print("0. Exit")

    menu = input("Select an option: ").strip()
    print(f"Received input: '{menu}'")  

    if menu == "1":
        contacts = add_contact.add_contact(contacts)
        load_save.save_contacts(contacts)  
    elif menu == "2":
        load_save.display_contacts(contacts)  
    elif menu == "3":
        name = input("Enter the name of the contact to update: ").strip()
        contacts = update_contact.update_contact(contacts, name)
        load_save.save_contacts(contacts)  
    elif menu == "4":
        query = input("Enter search query: ").strip()
        matching_contacts = search_contact.search_contacts(contacts, query)
        load_save.display_contacts(matching_contacts)
    elif menu == "5":
        name = input("Enter the name of the contact to remove: ").strip()
        contacts = remove_contact.remove_contact(contacts, name) 
        load_save.save_contacts(contacts)
    elif menu == "0":
        load_save.save_contacts(contacts)  
        print("Contacts saved successfully. Goodbye!")
        break      
    else:
        print("Invalid option, please try again.")
