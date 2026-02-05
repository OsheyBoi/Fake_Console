import sys
import time
import random
import getpass
import Login
name = "NA"
def start_program():
    print("Loading...")
    time.sleep(1)
    id = random.randint(1,9)
    ip = ("10.0.0." + str(id))
    print("Name: " + name)
    print("IP: " + ip)
    print("Location: Unknown")
    time.sleep(1)
    print("info Complete")
    time.sleep(1)
    input("Press Enter to return to menu")
    Login.menu()

def userid(user):
    global name
    name = user

# This part ensures the code only runs when called
if __name__ == "__Login__":
    start_program()
