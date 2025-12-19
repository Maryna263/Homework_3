def input_error(func):
    """Декоратор для обробки помилок введення користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"Error: {e}"
    return inner

def parse_input(user_input):
    """Розбирає введений рядок на команду та аргументи."""
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    """Додає новий контакт або оновлює існуючий."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    """Виводить номер телефону для зазначеного контакту."""
    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts):
    """Виводить всі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    print("Доступні команди: 'hello', 'add [ім'я] [телефон]', 'change [ім'я] [телефон]', 'phone [ім'я]', 'all', 'close' або 'exit'.")
    
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()