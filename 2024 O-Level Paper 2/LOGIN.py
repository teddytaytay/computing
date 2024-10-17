list_usernames = ["StudentNol", "JaneJones", "ABC123"]
while True:
    username = input("Please enter a username: ")
    if username not in list_usernames:
        list_usernames.append(username)
        break
    else:
        print("This username already exists. Please try again.")
        continue
while True:
    password = input("Please enter a password: ")
    if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" not in password:
        print("Please include at least 1 numeric character.")
        continue
    if "@" or "!" or "/" or "?" not in password:
        print("Please include at least 1 special character (@!/?).")
        continue 
    if password.length() < 8:
        print("The password must be at least 8 characters in length.")
        continue
    else: break
print(username, " ", list_usernames, " ", password) 
         