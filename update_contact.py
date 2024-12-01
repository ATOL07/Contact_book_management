def update_contact(contacts, name):
 
    for contact in contacts:
        if contact["Name"].lower() == name.lower():
            print(f"Updating details for {contact['Name']}")
            contact["Name"] = input(f"Enter updated name ({contact['Name']}): ").strip() or contact["Name"]
            contact["Email"] = input(f"Enter new email ({contact['Email']}): ").strip() or contact["Email"]
            contact["Phone"] = input(f"Enter new phone number ({contact['Phone']}): ").strip() or contact["Phone"]
            contact["Address"] = input(f"Enter new address ({contact['Address']}): ").strip() or contact["Address"]
            print(f"Information Updated for {contact['Name']}")
            return contacts
    print("Contact not found.")
    return contacts

