import string
import random

def generate_password():
    print("Password Generator")
    try:
        length = int(input("How long do you want your password? (min 4): ").strip())
    except ValueError:
        print("Error: Please enter a valid number.")
        return

    if length < 4:
        print("Error: Password should be at least 4 characters.")
        return

    include_letters = input("Include letters? (y / n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y / n): ").strip().lower() == 'y'
    include_symbols = input("Include symbols? (y / n): ").strip().lower() == 'y'

    letters = string.ascii_letters if include_letters else ''
    numbers = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    all_chars = letters + numbers + symbols

    if not all_chars:
        print("Error: You must include at least one type of character.")
        return

    password = []

    if include_letters:
        password.append(random.choice(letters))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_symbols:
        password.append(random.choice(symbols))

    remaining = length - len(password)
    password += random.choices(all_chars, k=remaining)

    random.shuffle(password)

    final_password = ''.join(password)
    print(f"Your generated password is: {final_password}")

generate_password()
