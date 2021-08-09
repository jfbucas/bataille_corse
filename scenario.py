class Scenario:
	def __init__(self, samples, names, means, contracts, exclude=[]):
		self.samples = samples
		self.names = names
		self.snap_means = means
		self.cards_contracts = contracts
		self.exclude_cards_with_value = exclude
