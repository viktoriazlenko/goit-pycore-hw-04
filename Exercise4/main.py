# This is a simple assistant bot that can manage contacts. 
# It allows you to add, change, and show contacts, as well as exit the program.
# The bot recognizes the following commands:
# - "hello": The bot will greet you and ask how it can help you.
# - "add [name] [phone]": The bot will add a new contact with the provided name and phone number.
# - "change [name] [phone]": The bot will update the phone number of an existing contact with the provided name.
# - "phone [name]": The bot will show the phone number of the contact with the provided name.
# - "all": The bot will show all contacts in the contact list.
# - "close" or "exit": The bot will say goodbye and exit the program.
 


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()




def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try: 
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid input. Please provide both name and phone number."

def change_username_phone(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid input. Please provide both name and phone number."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
    
def show_all(args, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."
    


