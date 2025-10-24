print("Welcome to the secure system.")



entered_pin = ""
correct_pin = 1234
max_attempts = 3
attempts = 0





while attempts < max_attempts:
    
    print(f"attempt {attempts + 1} of {max_attempts}")
    
    entered_pin = input("Please enter your PIN: ")
    if entered_pin == correct_pin:
        print("Access granted. Welcome!")
        break  # Exit the loop if the PIN is correct
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")
        if attempts == max_attempts:
           
           
           
            print("pin is incorrect,access denied")

