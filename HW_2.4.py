def add_contact(args, contacts):
    """Додає новий контакт у словник."""
    try:
        username, phone = args.split()
        contacts[username] = phone
        return f"Контакт '{username}' з номером '{phone}' додано."
    except ValueError:
        return "Помилка: Неправильний формат команди. Використовуйте: 'add [ім'я] [телефон]'."

def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    try:
        username, phone = args.split()
        if username in contacts:
            contacts[username] = phone
            return f"Номер телефону для контакту '{username}' змінено на '{phone}'."
        else:
            return f"Помилка: Контакт '{username}' не знайдено."
    except ValueError:
        return "Помилка: Неправильний формат команди. Використовуйте: 'change [ім'я] [телефон]'."

def show_phone(args, contacts):
    """Повертає номер телефону для вказаного контакту."""
    try:
        username = args.strip()
        if username in contacts:
            return f"Номер телефону для контакту '{username}': {contacts[username]}"
        else:
            return f"Помилка: Контакт '{username}' не знайдено."
    except ValueError:
        return "Помилка: Неправильний формат команди. Використовуйте: 'phone [ім'я]'."

def show_all(contacts):
    """Повертає рядок з усіма збереженими контактами."""
    if not contacts:
        return "Наразі немає збережених контактів."
    else:
        result = "Всі контакти:\n"
        for username, phone in contacts.items():
            result += f"{username}: {phone}\n"
        return result.strip()

def handle_exit():
    """Обробляє команду виходу."""
    return "Good bye!"

def main():
    """Основна функція взаємодії з користувачем."""
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    print("Доступні команди: 'hello', 'add [ім'я] [телефон]', 'change [ім'я] [телефон]', 'phone [ім'я]', 'all', 'close' або 'exit'.")

    while True:
        user_input = input("Введіть команду: ").lower().strip()
        
        if user_input in ["close", "exit"]:
            print(handle_exit())
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input.startswith("add "):
            args = user_input[4:]
            print(add_contact(args, contacts))
        elif user_input.startswith("change "):
            args = user_input[7:]
            print(change_contact(args, contacts))
        elif user_input.startswith("phone "):
            args = user_input[6:]
            print(show_phone(args, contacts))
        elif user_input == "all":
            print(show_all(contacts))
        else:
            print("Невідома команда. Будь ласка, спробуйте ще раз.")

if __name__ == "__main__":
    main()
    def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Invalid command format or missing argument."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError
    