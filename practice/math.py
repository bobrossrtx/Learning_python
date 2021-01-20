
input_string = input("What is 6 + 6 = ")

if input_string == "12":
    answer = True
elif input_string != "12":
    answer = False

if answer == True:
    print(f"Correct Answer : {input_string}")
elif answer == False:
    print(f"Wrong Answer : {input_string}")

print("")

input_string = input("What is 14 + 67 = ")

if input_string == "81":
    answer = True
elif input_string != "81":
    answer = False

if answer == True:
    print(f"Correct Answer : {input_string}")
elif answer == False:
    print(f"Wrong Answer : {input_string}")

print("")

input_string = input("What is 107 * 63 = ")

if input_string == "6741":
    answer = True
elif input_string != "6741":
    answer = False

if answer == True:
    print(f"Correct Answer : {input_string}")
elif answer == False:
    print(f"Wrong Answer : {input_string}")

if (answer, answer, answer) == (True, True, True):
    print("Well done, You got all the answers correct")
elif (answer, answer, answer) == (False, True, True):
    print("You got the 1st answer incorrect. :(")
elif (answer, answer, answer) == (True, False, True):
    print("You got 2nd answer incorrect. :(")
elif (answer, answer, answer) == (True, True, False):
    print("You got 3rd answer incorrect. :(")
elif (answer, answer, answer) == (False, False, True):
    print("You got the 1st and 2nd answer incorrect. :(")
elif (answer, answer, answer) == (True, False, False):
    print("You got 2nd and 3rd answer incorrect. :(")
elif (answer, answer, answer) == (False, True, False):
    print("You got 1st and 3rd answer incorrect. :(")
elif (answer, answer, answer) == (False, False, False):
    print("Wow, you need to attend your maths classes. :(")

