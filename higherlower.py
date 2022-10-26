from art import highlow,vs
import random
from game_data import data
import os

game_ends = False
score = 0
account2 = random.choice(data)

# def compare():
print(highlow)
def format_data(account):
    """Formats data and prints in prinatable format"""
    account_name = account["name"]
    # followers = account["follower_count"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take Guessessed input from user and both accounts followers count and return true or false"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


while not game_ends:
    account1 = account2
    account2 = random.choice(data)

    while account1 == account2:
        account2 = random.choice(data)

    print(f"Compare A {format_data(account1)}")
    print(vs)
    print(f" against B, {format_data(account2)}")
    guess = input("Which person has more number of followers. Type 'a' or 'b' ").lower()

    a_followers = account1["follower_count"]
    b_followers = account2["follower_count"]
    # print(a_followers, b_followers)
    output = check_answer(guess, a_followers, b_followers)
    print(output)
    if output:
        score += 1
        os.system("clear")
        print(f"You are correct, your score is {score}")
    else:
        print(f"Sorry its incorrect, your Final Score is : {score}")
        game_ends = True



