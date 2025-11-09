

passwords =  [
    "passbird",
    "weak",
    "123456789",
    "P!rat3ed"

]

#dictionary of bad passwords 



for password in passwords:
    length_ok = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_specdigit = any(c.isdigit() for c in password)

    if length_ok and has_upper and has_lower and has_specdigit:
        print(f"complaint : {password}")

    else:
        print(f"non-complaint:{password}")

        if not length_ok:
            print("-fails: needs to have length of 8 letters")

        if not has_upper:
            print("-fails: needs upper digit ")    


        if not has_lower:
            print("-fails: needs lower digit ")

        if not has_specdigit:
            print("- fails: need to have special ")




