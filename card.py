class Card:

	default_contracts = { "A":4, "K":3, "Q":2, "J":1 }

	def __init__(self, color, value, contracts={}):
		self.color = color
		self.value = value
		self.contract = None

		if value in contracts:
			self.contract = contracts[value]
		elif value in self.default_contracts.keys():
			self.contract = self.default_contracts[value]

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
