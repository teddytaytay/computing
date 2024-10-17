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
    if not password.alnum():
        print("Please include at least 1 numeric character.")
        continue
    spc_char_list = ["@", "!", "/", "?"]
    if spc_char_list not in password:
        print("Please include at least 1 special character (@!/?).")
        continue 
    if password.length() < 8:
        print("The password must be at least 8 characters in length.")
        continue
    else: break
print(username, " ", list_usernames, " ", password) 
         