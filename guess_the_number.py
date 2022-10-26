from random import randint
# numbers = []
# for number in range(1,101):
#     numbers.append(number)

# print(numbers)
guess_number = randint(1, 100)

# print(guess_number)

print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
diffculty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diffculty == "easy":
    chances = 10
elif diffculty == "hard":
    chances = 5

while chances != 0:
    print(f"You have {chances} attempts left")
    user_guess = int(input("Make a Guess: "))
    chances -= 1
    if user_guess < guess_number:
        print("Too low")
    elif user_guess > guess_number:
        print("Too high")
    elif user_guess == guess_number:
        print(f"You guessed it, the answer was {guess_number}")
        chances = 0