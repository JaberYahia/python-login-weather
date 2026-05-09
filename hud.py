from create import create_User
from login import login_page



while True: 
    print("what would you like to do?")
    print("1. Create user")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Pick your choice: "))

    if choice ==  1:
        create_User()
    if choice == 2:
        login_page()
    if choice == 3:
        quit()

