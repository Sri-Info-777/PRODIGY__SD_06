
import random

print("===================================")
print("       NUMBER GUESSING GAME")
print("===================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess the correct number!")

while True:
    try:
        guess = int(input("\nEnter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print("\nCongratulations! You guessed correctly!")
            print("The correct number was:", secret_number)
            print("Total attempts:", attempts)
            print("Thank you for playing!")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")
