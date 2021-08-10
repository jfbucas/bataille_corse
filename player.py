import random

class Player:
	
	def __init__(self, name, snap_percent=None):
		
		self.name  = name

		self.snap_percent = snap_percent

		self.win_count = 0
		self.snap_count = 0
		self.hand = []
		self.next_player = None


	def __str__(self):
		return self.name.rjust(10, ' ')
		#return self.name+"("+str(len(self.hand))+")"
	
	def __repr__(self):
		return self.__str__()
	
	def __add__(self, other):
		return str(self) + other
	
	def __radd__(self, other ):
		return other + str(self)
	
	def wins(self):
		self.win_count += 1
	
	def winsSnap(self):
		self.snap_count += 1
	
	def getSnaps(self):
		return self.snap_count
	
	def getSnapTime(self):
		return self.snap_percent
	
	def hasMadeAMistake(self):
		# TODO : player can get confused with cards designs and snap incorrectly
		return False
	
	def remembersPair(self, cardA, cardB):
		# TODO : player can remember a pair
		return False
	
	def addCardToHand(self, card):
		self.hand.append( card )

	def resetHand(self):
		self.hand = []

	def playCard(self):
		card = None
		if len(self.hand) > 0:
			card = self.hand.pop(0)
		return card

	def hasLost(self):
		return len(self.hand) == 0

	def hasCards(self):
		return len(self.hand) != 0

	def setNextPlayer(self, player):
		self.next_player = player

	def nextPlayer(self):
		return self.next_player

	# a little arrangement between friends
	def exchangeCardsWithPlayer(self, values, player):
		for c in player.hand:
			if c.value in values:
				player.hand.remove(c)
				player.hand.append( self.hand.pop(0) )
				self.hand.append(c)

