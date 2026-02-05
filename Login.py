import sys
import time
import random
import string
import Accountstatus
import incrypter
global username, User
User = ("NA")
username = (str("na"))
# --- CIPHER SETUP ---
# Standard alphabet for mapping
alphabet = string.ascii_lowercase
# Your specific secret mapping (26 unique characters)
secret_key = "qazplmwsxokndcijbrefvtghuy"
# Create the encryption table
cipher_table = str.maketrans(alphabet, secret_key)
def encrypt_password(password):
    """Converts plain text password into the ciphered version."""
    return password.lower().translate(cipher_table)


def checklogin(user_input, pass_input):
    # Encrypt the input password so it matches the secret format in the file
    encrypted_input_pass = encrypt_password(pass_input)

    try:
        with open("login.txt", "r") as file:
            for line in file:
                # Ensure the line has a colon before splitting
                if ":" in line:
                    stored_user, stored_pass = line.strip().split(":")
                    if user_input == stored_user and encrypted_input_pass == stored_pass:
                        return True
    except FileNotFoundError:
        print("Error: login.txt not found.")
    return False
print ("Please enter the Username:")
username = input()
username = str(username)
print ("Please enter the Password:")
inputcode = input()
inputcode = str(inputcode)
if checklogin(username, inputcode):
    print ("Access granted")
    time.sleep(1)
    print ("Loading...")
else:
    print ("Access Denied")
    sys.exit()
time.sleep(1)
print ("Welcome " + username)
time.sleep(1)
print ("What  would you like to do?")
print ("[1] Access Account Status")
print ("[2] Access Server status")
print ("[3] User Setting")
print ("[4] Log Out")
option = input()
if option == str(1):
    Accountstatus.userid(username)
    Accountstatus.start_program()
if option == str(3):
    incrypter.main_menu()