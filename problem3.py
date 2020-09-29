#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks
uname=input("Enter a username ")
realUname="admin" in uname
if realUname==False:
    print("invalid user")
    quit()

pword=input("Enter a password ")
if pword != "12345password":
    print("incorrect password")
    quit()
elif pword=="12345password":
    print("Access granted")

    
