import random

while True:
    user = input("Roll the dice? (y/n) : ").lower()
    if user == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")

    elif user == 'n':
        print("Thanks for playing")
        break

    else:
        print("Invalid choice!")
