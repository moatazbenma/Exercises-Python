import random 

choices = ['r', 's', 'p']

def get_user_choice():
    while True:
        user = input("Rock, paper, or scissors? (r/p/s): ").lower()
    
        if user in choices:
            return user
        else:
            print("Invalid choice!")

def display_choices(user, computer_choice):
    print(f"You chose {user}")
    print(f"Computer chose {computer_choice}")


def determine_winner(user, computer_choice):
    if (user == 'r' and computer_choice == 's') or \
       (user == 's' and computer_choice == 'p') or \
       (user == 'p' and computer_choice == 'r'):
        print("You won!")
    elif user == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")

            
def play_game():
    while True:
        user = get_user_choice()
        computer_choice = random.choice(choices)
    
        display_choices(user, computer_choice)

        determine_winner(user, computer_choice)

        then_continue = input("Do you want to continue? (y/n): ").lower()
        if then_continue == 'n':
            print("Goodbye!")
            break

play_game()