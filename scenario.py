class Scenario:
	def __init__(self, games, names, means, contracts, exclude=[]):
		self.games = games
		self.names = names
		self.snap_means = means
		self.cards_contracts = contracts
		self.exclude_cards_with_value = exclude
