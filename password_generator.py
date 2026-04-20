import secrets
import string

def password_generator(length, use_upper, use_numbers, use_symbols):
    
    password = ""

    chars = string.ascii_lowercase

    if use_upper == "y":
        chars += string.ascii_uppercase
    if use_numbers == "y":
        chars += string.digits
    if use_symbols == "y":
        chars += string.punctuation
     
    for i in range(length):
        password += secrets.choice(chars)
        
    return password


def main():
    try:
        pass_length = int(input("Enter the password length: "))

        if pass_length < 6:
            print("Error: Password must be at least 6 characters long")
            return

        is_uppercase = input("Include uppercase (y/n): ").lower()
        is_numbers = input("Include numbers (y/n): ").lower()
        is_symbols = input("Include symbols (y/n): ").lower()

        password = password_generator(pass_length, is_uppercase, is_numbers, is_symbols)
        print(f"The password is: {password}")

    except ValueError:
        print("Error: Please enter a valid number")


if __name__ == "__main__":
    main()