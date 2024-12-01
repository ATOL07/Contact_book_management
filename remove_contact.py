def remove_contact(contacts, name):
    
    updated_contacts = [contact for contact in contacts if contact["Name"].lower() != name.lower()]
    
    if len(updated_contacts) < len(contacts):
        print(f"Contact '{name}' has been removed.")
    else:
        print(f"Contact '{name}' not found.")
    
    return updated_contacts
