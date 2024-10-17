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
    if not any(char.isdigit() for char in password):
        print("Please include at least 1 numeric character.")
        continue
    if not any(char in "!@/?" for char in password):
        print("Please include at least 1 special character (@!/?).")
        continue 
    if len(password) < 8:
        print("The password must be at least 8 characters in length.")
        continue
    else: break
print(username, " ", list_usernames, " ", password) 
         