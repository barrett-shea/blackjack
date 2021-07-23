'''
Python Casino of Las Vegas
Black Jack 21

Rules:
        1) Aim of game is to achieve a hand whose points total nearer to 21 than dealer's hand, without going over.
        2) 6 decks shuffled. Blackjack pays 3 to 2.
        3) Dealer must hit up to soft 17. Must stand on a hard 17 and higher.
        4) Minimum bet size $5.

How to Play:
        1) Enter number of players (1-4)
        2) Enter beginning chip amount.
        3) Play begins with players entering bet size.
        4) Once dealt, players have choice to stand, hit, split, and double down.
'''

import random, ui


deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

## four suits and playing with six decks

def shuffle(deck):
	global shoe
	shoe = deck*4*6
	random.shuffle(shoe)


# add players
while True:  #input validation
	print('Enter the number of players (1-4).')
	playerCount = input()
	try:
		playerCount = int(playerCount)
	except ValueError:
		print('Please enter a numerical digit.')
		continue
	if (playerCount < 1 or playerCount > 4):
		print('Please enter a number between 1 and 4.')
		continue
		# input successful
	break
	
	
# purchase chips. Need to add validation.
chips = []
for player in range(playerCount):
	bet = int(input('Input Player ' + str(player+1) + ' chip purchase. $'))
	chips.append(bet)

	
# sum current value of hand
def total(hand):
	total = 0
	for card in hand:
		if card == "J" or card == "Q" or card == "K":
			total+= 10
		elif card == "A":
			if total >= 11: total+= 1
			else: total+= 11
		else:
			total += card
	return total
	
# hit a hand
def hit(player):
	card = shoe.pop()
	player.append(card)
	return
	
# place initial bets
tableBets = []
def bets(chips):
	for player in range(playerCount):
		while True:
			try:
				bet = int(input('Input Player ' + str(player+1) + ' bet. $'))
			except ValueError:
				print('Please enter a numerical digit.')
				continue
			if (bet < 5 or bet > chips[player]):
				print('Please enter a number less than your total chips, but at least 5.')
				continue
				# input successful
			break
		tableBets.append(bet)
		chips[player] -= bet
		
# deal cards to players + deal
table = []
dealerHand = []
def deal(shoe):
	for player in range(playerCount):
		table.append([])
		
	for i in range(2):
		for player in range(playerCount):
			table[player].append(shoe.pop())
		dealerHand.append(shoe.pop())
		
def clear():
	global table
	table = []
	global dealerHand
	dealerHand = []


def play():
	print("Let's play a hand!")
	bets(chips)
	deal(shoe)
	print("Player hands: " + str(table))
	print("Dealer showing: " + str(dealerHand[0]))
	
	
	for player in range(playerCount): #cycle thru players until they stand or bust
		choice = ""
		bustCount = 0
		while choice != "f":
			choice = input("Player " + str(player+1) + ": Take a hit? T or F").lower()
			
			if choice == "t":
				hit(table[player])
				print("Player hands: " + str(table))
				if total(table[player]) > 21:
					print("Sorry, Player " + str(player+1) + " you busted.")
					bustCount += 1
					break
	
	##if bustCount == playerCount:
		#dealer wins
		#payout function
		#else:
	# need to total player hands
	# dealer hits
	# identify winners
	# payout earnings/losses
	print("Trashing cards")
	clear()
	play()

shuffle(deck)
print(shoe) ## for testing purposes
play()


# wrap entire game in while loop if shoe != 0 ??
# if len(shoe) == 0:
		# shuffle(deck)
