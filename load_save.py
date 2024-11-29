def save_contacts(contacts):
    """
    Save the contacts list to 'contacts.csv' with a nice header,
    similar to the terminal output without commas.
    """
    with open("contacts.csv", "w") as fp:
        # Write the header with spaces (aligned)
        fp.write(f"{'Name':<20}{'Email':<25}{'Phone':<15}{'Address':<30}\n")
        
        # Write each contact's details in a new line with spaces for alignment
        for contact in contacts:
            line = f"{contact['Name']:<20}{contact['Email']:<25}{contact['Phone']:<15}{contact['Address']:<30}\n"
            fp.write(line)

def load_contacts():
    """
    Load contacts from 'contacts.csv' and return them as a list of dictionaries.
    This function assumes the CSV has the same structure without commas.
    """
    contacts = []
    try:
        with open("contacts.csv", "r") as fp:
            # Skip the header line
            fp.readline()

            # Read each line, split by the spaces and append it to the contacts list
            for line in fp:
                # Split by fixed-width columns (you can adjust based on your needs)
                name = line[:20].strip()
                email = line[20:45].strip()
                phone = line[45:60].strip()
                address = line[60:].strip()

                contacts.append({
                    "Name": name,
                    "Email": email,
                    "Phone": phone,
                    "Address": address
                })
    except FileNotFoundError:
        pass  # If the file doesn't exist yet, return an empty list.
    
    return contacts

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

# Example usage


