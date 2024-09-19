# Jonathan Nunez
# Date: 9/17/24
# Purpose: The driver for the tuffy titan contact list and the user interaction

import contacts

def print_menu():
    print("""
    *** TUFFY TITAN CONTACT MAIN MENU ***
    1. Print list
    2. Add contact
    3. Modify contact
    4. Delete contact
    5. Sort list by first name
    6. Sort list by last name
    7. Exit the program
    """)

def print_contacts(contact_list):
    print("================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    for i, contact in enumerate(contact_list):
        print(f"{i:<6}  {contact[0]:<20}  {contact[1]:<20}")
    print()

def main():
    contact_list = []
    
    while True:
        print_menu()
        choice = input("Enter menu choice: ")

        if choice == "1":
            print_contacts(contact_list)

        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            contacts.add_contact(contact_list, first_name=first_name, last_name=last_name)

        elif choice == "3":
            index = int(input("Enter the index number: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            if not contacts.modify_contact(contact_list, index=index, first_name=first_name, last_name=last_name):
                print("Invalid index number.")

        elif choice == "4":
            index = int(input("Enter the index number: "))
            if not contacts.delete_contact(contact_list, index=index):
                print("Invalid index number.")

        elif choice == "5":
            contacts.sort_contacts(contact_list, column=0)

        elif choice == "6":
            contacts.sort_contacts(contact_list, column=1)

        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
