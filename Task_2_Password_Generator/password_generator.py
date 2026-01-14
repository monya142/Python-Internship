import random
import string
def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")


def get_character_preferences():
    
    print("\nSelect character types to include:")
    include_letters = input("Include letters (a-z, A-Z)? (y/n): ").lower()
    include_numbers = input("Include numbers (0-9)? (y/n): ").lower()
    include_symbols = input("Include symbols (!@#$ etc)? (y/n): ").lower()

    characters = ""

    if include_letters == 'y':
        characters += string.ascii_letters
    if include_numbers == 'y':
        characters += string.digits
    if include_symbols == 'y':
        characters += string.punctuation

    if characters == "":
        print("\nError: You must select at least one character type!")
        return None

    return characters


def generate_password(length, characters):
  
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


def password_strength(password):

    strength = 0

    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Medium"
    else:
        return "Strong"


def main():
    print("=" * 40)
    print("        PASSWORD GENERATOR        ")
    print("=" * 40)

    length = get_password_length()
    characters = get_character_preferences()

    if characters is None:
        return

    password = generate_password(length, characters)
    strength = password_strength(password)

    print("\nGenerated Password:", password)
    print("Password Strength:", strength)
    print("\nThank you for using Password Generator!")
if __name__ == "__main__":
    main()
