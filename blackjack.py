from hashlib import new
import random
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(list):
    total = 0
    for i in list:
        total += i
    return total


print(logo)

user_hand = []
computer_hand = []
game_ends = False
# print(user_hand)

for i in range(2):
    user_hand.append(deal_card())
    computer_hand.append(deal_card())
user_total = score(user_hand)
computer_total = score(computer_hand)
print(f"Your Cards {user_hand}, Current Score is {user_total}")
print(f"Computer's First card is {computer_hand[0]}")

while computer_total < 17:
    computer_hand.append(deal_card())
    computer_total = score(computer_hand)
    # print(f"Computer Total : {computer_total}")


while not game_ends:
    user_input = (input("Type 'y' to deal another card or 'n' to Stand: ")).lower()
    # while computer_hand 
    if user_input == 'y':
        user_hand.append(deal_card())
        user_total = score(user_hand)
        print(f"Your cards :{user_hand} and the New User total : {user_total}")
    elif user_input == 'n':
        game_ends = True
        print(f"Your Final hand is {user_hand}, Final score is {user_total}")
        print(f"Computer's Final hand is {computer_hand}, Final score is {computer_total}")


if computer_total == user_total:
    print("It is a Draw")
elif computer_total == 21:
    print("Dealer has a BlackJack")
elif user_total == 21:
    print("You have a BlackJack")
elif computer_total > 21:
    print("Dealer got Busted, You Win")
elif user_total > 21:
    print("You got busted, Dealer Wins")
elif user_total > computer_total:
    print("You Win")
else:
    print("Dealer Wins")
        
