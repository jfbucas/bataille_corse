class Card:
	def __init__(self, color, value):
		self.color = color
		self.value = value
		self.contract = None

		if value == "A":
			self.contract = 4

		elif value == "K":
			self.contract = 3

		elif value == "Q":
			self.contract = 2

		elif value == "J":
			self.contract = 1

	def __str__(self):
		return self.value
		return self.color+self.value
	
	def __add__(self, other):
		return str(self) + other
	
	def __radd__(self, other ):
		return other + str(self)
	
	def isSameValue(self, card):
		return self.value == card.value
	
	def hasAContract(self):
		return self.contract != None
