
contacts = []

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(contacts, 1):
                print(f"\nContact {i}")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "3":
        if not contacts:
            print("No contacts to edit.")
            continue

        try:
            number = int(input("Enter contact number to edit: "))

            if 1 <= number <= len(contacts):
                contact = contacts[number - 1]

                name = input("New name (Enter to keep current): ")
                phone = input("New phone (Enter to keep current): ")
                email = input("New email (Enter to keep current): ")

                if name:
                    contact["name"] = name
                if phone:
                    contact["phone"] = phone
                if email:
                    contact["email"] = email

                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        if not contacts:
            print("No contacts to delete.")
            continue

        try:
            number = int(input("Enter contact number to delete: "))

            if 1 <= number <= len(contacts):
                removed = contacts.pop(number - 1)
                print(removed["name"], "deleted successfully!")
            else:
                print("Invalid contact number.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "5":
        print("Thank you for using the Contact Management System!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
