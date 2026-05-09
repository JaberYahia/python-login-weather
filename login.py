def login_page():
    username = input("Username: ")
    password = input("Password: ")

    with open("usrs.txt", "r") as file:
        users = file.readlines()

    for user in users:

        stored_username, stored_password = user.strip().split(",")

        if username == stored_username and password == stored_password:
            print("Login successful!") 
            return
        
    print("Invalid Credentials")
        
            
    
