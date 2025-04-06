import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        user = int(input("Guess the number between 1 and 100: "))
        if user == number_to_guess:
            print("Congratulations! You guessed the number.")
            break
        elif user > number_to_guess:
            print("Too high")
        elif user < number_to_guess:
            print("Too low")
    except ValueError:
        print("Invalid number")
        
    
        