'''
This is a simple assistant bot that can manage contacts. 
 It allows you to add, change, and show contacts, as well as exit the program.
 The bot recognizes the following commands:
 - "hello": The bot will greet you and ask how it can help you.
 - "add [name] [phone]": The bot will add a new contact with the provided name and phone number.
 - "change [name] [phone]": The bot will update the phone number of an existing contact with the provided name.
 - "phone [name]": The bot will show the phone number of the contact with the provided name.
 - "all": The bot will show all contacts in the contact list.
 - "close" or "exit": The bot will say goodbye and exit the program.
''' 
 


def parse_input(user_input): #The function takes a user input string, splits it into a command and its arguments, and returns the command in lowercase along with the arguments as a list.
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    commands = {
        "hello": lambda args: "How can I help you?",
        "add": lambda args: add_contact(args, contacts),
        "change": lambda args: change_username_phone(args, contacts),
        "phone": lambda args: show_phone(args, contacts),
        "all": lambda args: show_all(args, contacts),
        
    }


    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        handler = commands.get(command)

        if handler: 
            print(handler(args))
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


def add_contact(args, contacts):   #The function takes a list of arguments and a dictionary of contacts, tries to add a new contact to the dictionary using the provided name and phone number, and returns a message indicating whether the contact was added successfully or if there was an error with the input.
    try: 
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid input. Please provide both name and phone number."

def change_username_phone(args, contacts): #The function takes a list of arguments and a dictionary of contacts, tries to update the phone number of an existing contact in the dictionary using the provided name and new phone number, and returns a message indicating whether the contact was updated successfully, if the contact was not found, or if there was an error with the input.
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid input. Please provide both name and phone number."

def show_phone(args, contacts): #The function takes a list of arguments and a dictionary of contacts, tries to retrieve the phone number of a contact from the dictionary using the provided name, and returns the phone number if the contact is found or a message indicating that the contact was not found if it is not in the dictionary.
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."
    
def show_all(args, contacts): #The function takes a list of arguments and a dictionary of contacts, checks if there are any contacts in the dictionary, and returns a formatted string of all contacts and their phone numbers if there are any, or a message indicating that no contacts were found if the dictionary is empty.
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."
    


