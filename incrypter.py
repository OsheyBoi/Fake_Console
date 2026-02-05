import string
import os

# --- GLOBAL CIPHER CONFIG ---
# These are placed here so all functions can use them
alphabet = string.ascii_lowercase
secret_key = "qazplmwsxokndcijbrefvtghuy"
encrypt_table = str.maketrans(alphabet, secret_key)
decrypt_table = str.maketrans(secret_key, alphabet)


def encrypt(text):
    """Applies your secret mapping to any string."""
    return text.lower().translate(encrypt_table)


def decrypt(text):
    """Reverses the secret mapping to show plain text."""
    return text.lower().translate(decrypt_table)


def add_user():
    print("\n--- Register New User ---")
    new_user = input("Enter new username: ").strip()
    new_pass = input("Enter new password: ").strip()

    # Encrypt before saving
    secret_pass = encrypt(new_pass)

    # Append to file
    with open("login.txt", "a") as file:
        file.write(f"{new_user}:{secret_pass}\n")

    print(f"User '{new_user}' added successfully with encrypted password!")


def encode_string():
    print("\n--- Quick Encoder ---")
    text = input("Enter text to convert to secret code: ")
    print(f"Secret Result: {encrypt(text)}")


def view_accounts():
    """Reads the file and decrypts the passwords for viewing."""
    print("\n--- Current Accounts (Decrypted) ---")
    if not os.path.exists("login.txt"):
        print("No login.txt file found.")
        return

    print(f"{'User':<15} | {'Password'}")
    print("-" * 30)

    with open("login.txt", "r") as file:
        for line in file:
            if ":" in line:
                stored_user, stored_pass = line.strip().split(":")
                # Decrypt the password here
                plain_pass = decrypt(stored_pass)
                print(f"{stored_user:<15} | {plain_pass}")


def main_menu():
    while True:
        print("\n[1] Add New User to login.txt")
        print("[2] Encode text to Secret Mapping")
        print("[3] View All Users/Passwords (Unencrypted)")
        print("[4] Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            encode_string()
        elif choice == "3":
            view_accounts()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


# Run the menu
if __name__ == "__Login_":
    main_menu()


