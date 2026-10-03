from contact_function import viewContacts, AddContact, DeleteContact, UpdateContacts, GetCommand, init_db

welcome_msg = '''
    =================================
       CONTACT MANAGER TERMINAL
    =================================
'''

command_msg = '''
    🔢 Enter [1] to view saved contacts
    🔢 Enter [2] to add contacts
    🔢 Enter [3] to edit contacts
    🔢 Enter [4] to delete saved contacts
    🔢 Enter [0] to exit
'''
def main():
    init_db()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact Phone")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = GetCommand()
        if choice == 1:
            AddContact()
        elif choice == 2:
            viewContacts()
        elif choice == 3:
            UpdateContacts()
        elif choice == 4:
            DeleteContact()
        elif choice == 5:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()