
def create_User():
    
        user_name = input("Please Enter username: ")

        while True:
         password = input("Please Enter password: ")
         if len(password) < 8:
            print("Password too short, Try again.") 
         else:
             break
   
        file = open ("usrs.txt", "a")
        file.write(user_name + "," + password + "\n")
        file.close()
        print("User created!")
            
        

        
     


