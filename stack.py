from card import Card

class Stack:
	def __init__(self):
		self.cards = []

	def __str__(self):
		return str(len(self.cards))
	
	def __add__(self, other):
		return str(self) + other
	
	def __radd__(self, other ):
		return other + str(self)
	
	def addCard(self, card):
		self.cards.append( card )

	def addCardAtBottom(self, card):
		self.cards.insert( 0, card )

	def winsCards(self, player):
		for card in self.cards:
			player.addCardToHand(card)
		self.cards = []
	
	def isSnapTime(self):
		if len(self.cards) >= 2:
			return self.cards[-1].isSameValue( self.cards[-2] )
		return False
