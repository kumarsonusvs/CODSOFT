import random
import string

def generate_password(length):
    # Define the character sets for password complexity
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user preferences
    all_chars = lowercase_chars + uppercase_chars + digits + special_chars

    # Ensure the password length is at least 8 characters
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate and display the password
    password = generate_password(length)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
