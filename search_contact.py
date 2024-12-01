def search_contacts(contacts, query):

    matching_contacts = []
    query = query.lower()
    for contact in contacts:
        if (query in contact["Name"].lower() or
                query in contact["Email"].lower() or
                query in contact["Phone"].lower() or
                query in contact["Address"].lower()):
            matching_contacts.append(contact)
    return matching_contacts
