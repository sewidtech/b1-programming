#rock-paper-scissors 

import random
def computerplay():
    
    choices = ["rock" , "paper" , "scissors"]
    choice = random.choice(choices)
    return choice

def userplay():
   
    print("Choose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Your choice (1-3): ").strip()

    if choice == "1":
        user_choice = "rock"
    elif choice == "2":
        user_choice = "paper"
    elif choice == "3":
        user_choice = "scissors"
    else:
        print("Invalid input.")
        return None

    print(f"User chose {user_choice}")
    return user_choice


def main():
    
    scores = {"user": 0 , "computer": 0 , "draws": 0 }
    
    

    
    while True :
        user_choice = userplay()
        if user_choice is None:
            continue
        computer_choice = computerplay()
        print(f"computer chose :{computer_choice}")
        if user_choice == computer_choice:
            print("its a draw")
            scores["draws"] += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock") :
            print("user won fairly")
            scores["user"] += 1
        else :
            print("computer won. \nwomp womp")
            scores["computer"] += 1

        



        leaderboard ={k: v for  k , v in sorted(scores.items() , key=lambda item :item[1], reverse = True)} 
        print(f"\nLeaderboard:")

        for player, score in leaderboard.items():
            print(f"{player}: {score}")

            
            print()

        play_again = input("\nPlay again? , yes or no : ").lower()
        
        
        if play_again == "yes":
            continue 
        else:
            print("Thank you for playing!!")
            break    

main()