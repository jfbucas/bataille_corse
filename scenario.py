class Scenario:
	def __init__(self, samples, names, means, contracts, exclude=[], cheat_jacks=False):
		self.samples = samples
		self.names = names
		self.snap_means = means
		self.cards_contracts = contracts
		self.exclude_cards_with_value = exclude
		self.cheat_jacks = cheat_jacks
	
	def __str__(self):
		return "Players: " + str(self.names) + " | Win % of Snaps: " + str(self.snap_means) + " | Contracts: " + str(self.cards_contracts) + " | Excluded: " + str(self.exclude_cards_with_value) + (" | Cheat Jacks! " if self.cheat_jacks else "")

	def __repr__(self):
		return self.__str__()
	
	def __add__(self, other):
		return str(self) + other
	
	def __radd__(self, other ):
		return other + str(self)
	
