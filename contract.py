class Contract:
	def __init__(self):
		self.remaining = None
		self.player    = None

	def __str__(self):
		return str(self.remaining)+" cards need to be played"
	
	def __repr__(self):
		return self.__str__()
	
	def __add__(self, other):
		return str(self) + other
	
	def __radd__(self, other ):
		return other + str(self)
	
	def isOngoing(self):
		return (self.remaining != None)
	
	def hasRunout(self):
		return (self.remaining == 0)
	
	def decRemaining(self):
		self.remaining -= 1

	def getRemaining(self):
		return self.remaining
	
	def getPlayer(self):
		return self.player

	def set(self, remaining, player):
		self.remaining = remaining
		self.player    = player
		
	def reset(self):
		self.remaining = None
		self.player    = None
	
		
