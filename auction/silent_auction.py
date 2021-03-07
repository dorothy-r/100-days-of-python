import art

print(art.logo)

cont = "yes"
bids = {}
while cont == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    cont = input("Are there others who want to bid? Enter 'yes' or 'no': ")
    print(f'\33c')

max_bid = 0
max_bidder = ""
for name in bids:
    if bids[name] > max_bid:
        max_bid = bids[name]
        max_bidder = name

print(f"The winner is {max_bidder}, with a bid of ${max_bid}.")
