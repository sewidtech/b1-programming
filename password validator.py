print("welcome to password validator")

#length


def min_length (password , min_length = 8 ):
        return len(password) >= min_length

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_lowercase(password):
     return any(c.islower() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)

def has_special_char(password):
    specials = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    return any(c in specials for c in password)

import random

lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specials = '!@#$%^&*()-_=+[]{};:\'",.<>?/\\|`~'

all_chars = lowercase + uppercase + digits + specials

def generate_random_password(length=8):
        password = ''.join(random.choice(all_chars) for _ in range(length))
        password = [
             random.choice(lowercase),
             random.choice(uppercase),
             random.choice(digits),
             random.choice(specials)
        ]    
             
       
             
         # Fill remaining characters randomly
        password += [random.choice(all_chars) for _ in range(length - 4)]
    
        random.shuffle(password)
        return ''.join(password)
        
        

def validate_password(password):
    results = {
        "Minimum length (8+)": min_length(password),
        "Uppercase letter": has_uppercase(password),
        "Lowercase letter": has_lowercase(password),
        "Number": has_digit(password),
        "Special character": has_special_char(password)
    }
    all_passed = all(results.values())
    return all_passed, results


#user interface 
def main():
    print("- Password Validation Program -")
    while True:
        print("\nOptions:")
        print("1. Enter password manually")
        print("2. Generate random password and test")
        print("3. Quit program")

        choice = input("Choose (1-3): ")

        if choice == '1':
            password = input("Enter password of your choice: ")
        elif choice == '2':
            password = generate_random_password()
            print(f"\nGenerated password: {password}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input, try again.")
            continue

        # Validate password
        valid, results = validate_password(password)
        print("\nValidation Results:")
        for rule, passed in results.items():
            status = " Passed" if passed else " Failed"
            print(f"{rule} : {status}")

        if valid:
            print(" Congratulations, your password is valid!\n")
        else:
            print(" Invalid password, try again.\n")
main()            
