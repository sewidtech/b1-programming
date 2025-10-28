#limited login attempts


def program():
    print("Welcome to the secure system.")

    correct_password = "1234"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print(f"Attempt {attempts + 1} of {max_attempts}")
        entered_password = input("Please enter your PIN: ")

        if entered_password == correct_password:
            print("Access granted.")
            return  # Exit the function after successful login
        else:
            attempts += 1
            print(f"Incorrect PIN. You are on attempt {attempts} of {max_attempts}.\n")

    # If the loop finishes, it means too many failed attempts
    print("Too many incorrect attempts. Access denied.")

# Run the program
program()



def menu():

    


    menu()









