#!/usr/bin/python3

from operator import itemgetter

from card import Card
from deck import Deck
from stack import Stack
from contract import Contract
from player import Player

def verbose(level, message):
	if level <= 0:
		print( message )

# Create the players
# LM2019 forever
players = []
for name in [ "Sophie", "Christelle", "Vincent", "Jef" ]:
	player = Player(name)
	if len(players) > 0:
		player.setNextPlayer(players[-1])
	players.append( player )
players[0].setNextPlayer(players[-1])

# The deck
deck = Deck()
deck.shuffle()
deck.distribute(players)


# Let's go!
stack = Stack()
turn = 0
player = players[ 0 ]


contract = Contract()

game_over = False
while not game_over:
	
	
	if player.hasCards():
		# Play a card
		card = player.playCard()
		stack.addCard(card)
		verbose( 1, stack+" "+player+" plays "+card )

		# Is it a pair?
		if stack.isSnapTime():
			snap_times = sorted([ [p, p.getSnapTime()] for p in players ], key=itemgetter(1))
			player = snap_times[0][0]
			stack.winsCards(player)
			player.winsSnap()
			verbose( 2, player+" wins the snap"+" ------------" )

		# New contract?
		elif card.hasAContract():
			contract.set(card.contract, player)
			verbose( 3, player+" sets contract: "+contract )
			player = player.nextPlayer()

		# Do we have a running contract?
		elif contract.isOngoing():
			contract.decRemaining()
			if contract.hasRunout():
				player = contract.getPlayer()
				verbose( 3, player+" wins contract" )
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

print()
winner = [ str(p) for p in players if p.hasCards() ][ 0 ]
print( winner+" wins after "+str(turn)+" turns " )
print()
for p in players:
	print( p+" snapped "+str(p.getSnaps())+" times" )
