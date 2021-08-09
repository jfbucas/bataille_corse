import random

from card import Card

class Deck:
	def __init__(self, exclude_values=None, contracts={}):
		self.cards = []

		possible_colors = [ "D", "S", "H", "C" ]
		possible_values = [ "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2" ]
		# TODO : joker

		# TODO : chien

		# Build the Deck
		for c in possible_colors:
			for v in possible_values:
				if exclude_values:
					if v in exclude_values:
						continue					
				self.cards.append( Card(c, v, contracts) )
	def __str__(self):
		s = ""
		for c in self.cards:
			s+=c+" "
		return s
	
	def __add__(self, other):
		return str(self) + other
	
	def __radd__(self, other):
		return other + str(self)
	
	def shuffle(self):
		random.shuffle(self.cards)

	def distribute(self, players):
		p = players[ 0 ]
		for c in self.cards:
			p.addCardToHand(c)
			p = p.nextPlayer()
