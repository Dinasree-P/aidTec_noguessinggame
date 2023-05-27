import random

print("Welcome to the Number Guessing Game!")

while True:
    name = input("What's your name? ")
    print(f"Hello, {name}! Lets start with the general instructions:")
    print(" I'm thinking of a number between 1 and 100.")
    print("You should guess the number within 10 attempts, otherwise game is over")

    guessno = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < guessno:
            print("That's a smaller number..please try again")
            print(f"Caution!! You have reached {attempts} attempt.")
        elif guess > guessno:
            print("That's a larger..please try again")
            print(f"Caution!! You have reached {attempts} attempt.")
        else:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"Game over! You couldn't guess the number. It was {guessno}.")

    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() != "yes":
        print("Thank you for playing!")
        break
