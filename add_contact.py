import load_save

def is_valid_email(email):
    if "@" in email and "." in email.split('@')[-1]:
        return True
    return False

def add_contact(contacts):
    while True:
        name = input("Enter Name: ").strip()
        if not name.isalpha():
            print("Name must be a string containing only letters.")
            continue
        break

    while True:
        email = input("Enter Email: ").strip()
        if not is_valid_email(email):
            print("Please enter a valid email address.")
            continue
        break

    while True:
        phone = input("Enter Phone Number: ").strip()
        if not phone.isdigit():
            print("Phone number must be an integer.")
            continue
        break

    while True:
        address = input("Enter Address: ").strip()
        if not address:
            print("Address must be a valid string.")
            continue
        break

    # Checking for duplicate phone numbers
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


