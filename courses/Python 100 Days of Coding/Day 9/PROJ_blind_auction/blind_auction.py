from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bids = {}
bidding_finished = False

def highest_bidder(bids):
    winner = 0
    for bidder in bids:


        
while not bidding_finished:
    print("Welcome to the secret auction program")
    name = input("What is you name?:")
    money = input("What's your bid?:")
    others = input("Are there any other bidders? Type 'yes' or 'no'.")
    bids[name] = money
    if others == "no":
        bidding_finished = True
        highest_bidder()
    elif others == "yes":
        clear()

