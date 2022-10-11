#from turtle import clear
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
end_script = True
highest_bid = 0
bidders = {}
winner = ""
print(logo)

def clrscr():
    # Check if Operating System is Mac and Linux or Windows
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # Else Operating System is Windows (os.name = nt)
      _ = os.system('cls')

while end_script:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid : $"))
  bidders[name] = bid
  another_bid = input("Are there any other bidders, yes or no").lower()
  if another_bid == "yes":
    clrscr()
  elif another_bid == "no":
    end_script = False

for person in bidders:
  if bidders[person] > highest_bid:
    highest_bid = bidders[person]
    winner = person
print(f"The highest bid from {winner} for {highest_bid}")
