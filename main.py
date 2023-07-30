def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter a valid name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter a name."
    return inner


class AddressBook:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, command):
        _, name, phone = command.split(' ')
        self.contacts[name] = phone
        return "Contact added."

    @input_error
    def change_phone(self, command):
        _, name, phone = command.split(' ')
        self.contacts[name] = phone
        return "Phone number updated."

    @input_error
    def get_phone(self, command):
        _, name = command.split(' ')
        return self.contacts[name]

    def show_all(self):
        if self.contacts:
            return '\n'.join([f'{name}: {phone}' for name, phone in self.contacts.items()])
        else:
            return "No contacts."


def main():
    address_book = AddressBook()

    while True:
        command = input("Enter a command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            result = address_book.add_contact(command)
            print(result)
        elif command.startswith("change"):
            result = address_book.change_phone(command)
            print(result)
        elif command.startswith("phone"):
            try:
                result = address_book.get_phone(command)
                print(result)
            except KeyError:
                print("Contact not found.")
        elif command == "show all":
            print(address_book.show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
