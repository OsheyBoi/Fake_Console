import Login
import time

def start(user):
    print("Loading...")
    time.sleep(1)
    print("Checking if User has Access Stats")
    if user == "OsheyBoi":
        print("Access granted")
        print("Server Status: Online")
        print("Location: Unknown")

        input("Press Enter to Exit")
        Login.menu()
    else:
        print("Access Denied")
        Login.menu()


if __name__ == "__Login__":
    start()
