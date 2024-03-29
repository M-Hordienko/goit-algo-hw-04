def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        return "Error: Contact not found in contacts"
    
    contacts[name] = phone

    return "Contact updated successfully"


def show_contact(args, contacts):
    name = args[0]

    if name not in contacts:
        return "Error: Can't find a phone number because contact not found in contacts"

    return contacts[name]


def show_all_contacts(contacts):
    return contacts


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
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()