#!/usr/bin/python3

import random
import os
from operator import itemgetter

from card import Card
from deck import Deck
from stack import Stack
from contract import Contract
from player import Player
from scenario import Scenario

# Output verbosity
VERBOSE = 0
if "VERBOSE" in os.environ:
	VERBOSE = int(os.environ["VERBOSE"])

def verbose(level, message):
	if level <= VERBOSE:
		print( message )



# Play a game
def gameOn(players, snap_chances):


	# Setup the Game
	stack = Stack()
	contract = Contract()
	turn = 0
	game_over = False

	# Pick the first player to start
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
			verbose( 3, stack+" "+player+" plays "+card )
			if player.hasLost():
				verbose( 4, stack+" "+player+" is out of cards" )

			# Is it a pair?
			if stack.isSnapTime():
				#snap_times = sorted([ [p, p.getSnapTime()] for p in players ], key=itemgetter(1))
				player = random.choice(snap_chances)
				verbose( 3, player+" wins the snap" )
				if player.hasLost():
					verbose( 4, stack+" "+player+" is back in the game" )
				stack.winsCards(player)
				player.winsSnap()

			# New contract?
			elif card.hasAContract():
				contract.set(card.contract, player)
				verbose( 5, player+" sets contract: "+contract )
				player = player.nextPlayer()

			# Do we have a running contract?
			elif contract.isOngoing():
				contract.decRemaining()
				if contract.hasRunout():
					player = contract.getPlayer()
					verbose( 5, player+" wins contract" )
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

	verbose(1, winner+" wins after "+str(turn)+" turns " )
	for p in players:
		verbose(2, p+" snapped "+str(p.getSnaps())+" times" )
	
	return turn




# Test a scenario many times
def runScenario( scenario ):

	# Create the players and link them
	players = []
	for name in scenario.names:
		if name in scenario.snap_means.keys():
			player = Player(name, scenario.snap_means[name])
		else:
			player = Player(name)
		if len(players) > 0:
			player.setNextPlayer(players[-1])
		players.append( player )
	players[0].setNextPlayer(players[-1])
	
	# Percentage of snap time to be distributed among players
	how_many_to_be_distributed = sum([ (p.snap_percent == None) for p in players ])
	snap_chances = []
	for p in players:
		if p.snap_percent != None:
			for i in range(p.snap_percent):
				snap_chances.append( p )
	leftover = (100 - len(snap_chances)) // how_many_to_be_distributed
	for p in players:
		if p.snap_percent == None:
			for i in range(leftover):
				snap_chances.append( p )


	# Create the Deck
	deck = Deck(scenario.exclude_cards_with_value, scenario.cards_contracts)

	# Run many times
	all_turns = []
	for i in range(0, scenario.samples):

		# Empty players hands
		for p in players:
			p.resetHand()

		# Shuffle the cards and distribute
		deck.shuffle()
		deck.distribute(players)

		# Start the game
		all_turns.append( gameOn(players, snap_chances) )

	# Show results
	verbose(0, "")

	total_snap_count = sum([ p.snap_count for p in players ])
	for p in players:
		verbose(0, p+" has won "+str(int(p.win_count*100/scenario.samples)).rjust(3,' ')+"% times and was first to snap "+ str(int(p.snap_count*100/total_snap_count)).rjust(3,' ')+"% of the time")

	verbose(0, "Min/Avg/Max number of turns "+ str(min(all_turns))+'/'+str(int(sum(all_turns)/len(all_turns)))+'/'+str(max(all_turns)))




# =========================

# LM2019 forever
players_names = [ "Jef", "Christelle", "Sophie", "Vincent", "Laetitia", "Gildas" ]
		

excluding_cards = [
			[],
			["2"],
			["2", "3"],
			["2", "3", "4"],
			["2", "3", "4", "5"],
		]

possible_contracts = [
			{ "A":4, "K":3, "Q":2, "J":1 },
			{ "J":1 },
			{}
		]


for samples in [ 1000 ]:

	for names in range(2, len(players_names)+1):

		for excluding in excluding_cards:

			for contracts in possible_contracts:

				for snap_mean in [ None ] + list(range(0, 110, 10)):

					scenario = Scenario(
						samples,
						players_names[:names], 
						{ "Jef":snap_mean },
						contracts,
						excluding,
					)

					verbose(0, ("-"*120) + "\n"+scenario)

					runScenario( scenario )

					verbose(0, "")


