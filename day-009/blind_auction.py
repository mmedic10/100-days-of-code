from replit import clear
from art import logo

more_bids = True
blind_dictionary = {}
print(logo)

while more_bids == True:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    other_bidder = input("Are there other any other bidders? Type 'yes' or 'no'").lower()
    blind_dictionary[name] = bid
    if other_bidder == 'no':
        more_bids = False
    clear()

greater = -1
winner = ""

for key in blind_dictionary:
    if blind_dictionary[key]>greater:
        greater = blind_dictionary[key]
        winner = key

print(f"The winner is {winner} with a bid of ${blind_dictionary[winner]}")



    

