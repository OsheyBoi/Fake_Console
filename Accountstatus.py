import sys
import time
import random
import getpass
name = "NA"
def start_program():
    print("Loading...")
    time.sleep(1)
    id = random.randint(1,9)
    ip = ("10.0.0." + str(id))
    print("Name: " + name)
    print("IP: " + ip)


def userid(user):
    global name
    name = user

# This part ensures the code only runs when called
if __name__ == "__Login__":
    start_program()
