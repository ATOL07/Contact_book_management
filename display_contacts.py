def display_contacts(contacts):
    """
    Display the contacts in a well-formatted way, similar to CSV output.
    """
    if not contacts:
        print("No contacts available.")
        return

    # Print the header for the contact table
    header = f"{'Name':<20}{'Email':<25}{'Phone':<15}{'Address':<30}"
    separator = "-" * len(header)

    print("\n" + separator)
    print(header)
    print(separator)

    # Print each contact's details in a formatted row
    for contact in contacts:
        print(f"{contact['Name']:<20}{contact['Email']:<25}{contact['Phone']:<15}{contact['Address']:<30}")
    
    print(separator)