

# TODO-1: Ask the user for input
import art
print(art.logo)
# TODO-2: Save data into dictionary {name: price}
Auction = {}
# TODO-3: Whether if new bids need to be added
is_there_bidder = True
while is_there_bidder:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    Auction[name] = bid
    if input("Are there any other bidders? Type Yes or No: ").lower() == "no":
        is_there_bidder = False
    else:
        print(f"\n"*100)
# TODO-4: Compare bids in dictionary

Winner_name = ""
Winner_bid = 0
for key in Auction:
    if Auction[key] > Winner_bid:
        Winner_name = key
        Winner_bid = Auction[key]
print(f"The winner is '{Winner_name}' with the bid is ${Winner_bid}")
