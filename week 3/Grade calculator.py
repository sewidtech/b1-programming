print("grade calculator")

input("Press Enter to check your grade")

score = int(input("Enter your score out of 100: "))
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")
else:
    print(f"you failed with a score of {score}")
    