#!/usr/bin/python3

import random
from operator import itemgetter

from card import Card
from deck import Deck
from stack import Stack
from contract import Contract
from player import Player

def verbose(level, message):
	if level <= 0:
		print( message )


# Play a game
def gameOn(players):
	for p in players:
		p.resetHand()

	# Create the Deck
	#deck = Deck(exclude_values=["2", "3", "4", "5"])
	deck = Deck()
	deck.shuffle()
	deck.distribute(players)


	# Setup the Game
	stack = Stack()
	contract = Contract()
	turn = 0
	game_over = False

	# Start player
	player = players[ 0 ]
	for i in range(random.randint(0, 100)):
		player = player.nextPlayer()


	# Let's go!
	while not game_over:
		
		# Has the player any cards
		if player.hasCards():
			# Play a card
			card = player.playCard()
			stack.addCard(card)
			verbose( 1, stack+" "+player+" plays "+card )
			if player.hasLost():
				verbose( 2, stack+" "+player+" is out of cards" )

			# Is it a pair?
			if stack.isSnapTime():
				snap_times = sorted([ [p, p.getSnapTime()] for p in players ], key=itemgetter(1))
				player = snap_times[0][0]
				verbose( 3, player+" wins the snap" )
				if player.hasLost():
					verbose( 2, stack+" "+player+" is back in the game" )
				stack.winsCards(player)
				player.winsSnap()

			# New contract?
			elif card.hasAContract():
				contract.set(card.contract, player)
				verbose( 4, player+" sets contract: "+contract )
				player = player.nextPlayer()

			# Do we have a running contract?
			elif contract.isOngoing():
				contract.decRemaining()
				if contract.hasRunout():
					player = contract.getPlayer()
					verbose( 4, player+" wins contract" )
					stack.winsCards(player)
					contract.reset()
			# Next player
			else:
				player = player.nextPlayer()

		else:
			# Go to next player
			player = player.nextPlayer()
			continue
		
		turn += 1

		# Game is over when only one player remains
		game_over = (sum([ p.hasCards() for p in players ]) == 1)

	winner = [ p for p in players if p.hasCards() ][ 0 ]
	winner.wins()

	verbose(0, winner+" wins after "+str(turn)+" turns " )
	for p in players:
		verbose(2, p+" snapped "+str(p.getSnaps())+" times" )



# =========================

# Create the players
# LM2019 forever
players = []
for name in [ "Sophie", "Christelle", "Vincent", "Jef" ]:
	player = Player(name)
	if len(players) > 0:
		player.setNextPlayer(players[-1])
	players.append( player )
players[0].setNextPlayer(players[-1])


# Run many times
for i in range(0, 1000):
	gameOn(players)

# Show results
print()
for p in players:
	print(p, "has won", p.win_count, "times")
