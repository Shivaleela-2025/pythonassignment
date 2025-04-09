#2.Write a program to check login credentials. If username is "admin" and password is "1234", print "Login successful", else "Invalid credentials".
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")
