

class Pokemon:
	def __init__(self, name: str, level: int, base_stats: list[int], base_stat_total: int, types: list[str], ability: str, ivs: list[int], evs: list[int], nature: str):
		self.name = name
		self.level = level
		self.base_stats = base_stats
		self.base_stat_total = base_stat_total
		self.types = types
		self.ability = ability
		self.ivs = ivs
		self.evs = evs
		self.nature = nature

def pokemon_generator() -> dict:
	name = input("Name: ")
	level = 100
	base_stats = []
	for i in range(6):
		base_stats.append(int(input(f"Enter Base Stat #{i+1}: ")))
	base_stat_total = sum(base_stats)
	types = []
	type1 = input(f"Enter Type #1: ")
	types.append(type1)
	type2 = input(f"Enter Type #2 (leave blank if none): ")
	if type2 == "":
		type2 = type1
	types.append(type2)
	ability = input(f"Enter the Ability: ")
	ivs = []
	for i in range(6):
		ivs.append(int(input(f"Enter IV #{i+1}: ")))
	evs = []
	for i in range(6):
		evs.append(int(input(f"Enter EV #{i+1}: ")))
	nature = input("Enter Nature: ")

	pokemon = Pokemon(name, level, base_stats, base_stat_total,types,ability,ivs,evs,nature)
	print(pokemon.__dict__)
	return pokemon.__dict__

pokemon_generator()