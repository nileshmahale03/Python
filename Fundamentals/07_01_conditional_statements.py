#if, elif, else

#1
age = int(input("enter your age:"))

if age < 13:
    print("child")
elif age >= 13 and age < 18:
    print("teenager")
elif age >= 18:
    print("adult")
else:
    print("wrong age entered") 


#Nesting
# Login System

username = input("enter username: ")
password = input("enter password: ")

if (username == "admin" and password == "pass"):
    print("log in successful!")
else:
    if username != "admin":   # NESTING
        print("wrong user name, try again.")
    else:
        print("wrong password, try again.")
