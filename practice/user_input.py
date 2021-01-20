print("Please enter your UserName:")
user_name = input()

if user_name == "":
    print("You need to enter your UserName")
    user_name = input()
    if user_name == "":
        print("You need to enter your UserName:")
        user_name = input()
    else: 
        print("Please enter your Email:")
        email = input()
else:
    print("Please enter your Email:")
    email = input()
    if email == "":
        print("You need to enter your Email:")
        email = input()
        if len(email) >= 1:
            output = f"Your userName is: {user_name}, and your email is: {email}"
            print(output)
        else:
            print("You need to enter your Email:")
            email = input()
    else: 
        output = f"Your userName is: {user_name}, and your email is: {email}"
        print(output)