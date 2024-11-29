import load_save

def add_contact(contacts):
    """
    Add a new contact to the list and save automatically.
    """
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    # Check for duplicate phone numbers
    for contact in contacts:
        if contact["Phone"] == phone:
            print("A contact with this phone number already exists.")
            return contacts

    # Append the new contact as a dictionary to the list
    contacts.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
    print("Contact added successfully!")

    # Automatically save after adding the contact
    load_save.save_contacts(contacts)

    return contacts
