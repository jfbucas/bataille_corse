import random

class Player:
	
	def __init__(self, name, snap_mean=None, snap_deviation=None):
		
		self.name  = name

		self.snap_mean      = 50
		self.snap_deviation = 10
		if snap_mean != None:
			self.snap_mean      = snap_mean
		if snap_deviation != None:
			self.snap_deviation = snap_deviation

		self.win_count = 0
		self.snap_count = 0
		self.hand = []
		self.next_player = None


	def __str__(self):
		return self.name
		return self.name+"("+str(len(self.hand))+")"
	
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
	
	def getSnapTime(self, cardA=None, cardB=None):
		# TODO : player can get confused with cards designs
		return random.gauss(self.snap_mean, self.snap_deviation)
	
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

