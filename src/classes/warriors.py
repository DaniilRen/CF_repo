class Warrior:
	def __init__(self, name, weapon, warrior_type, stamina) -> None:
		self.stamina = stamina
		self.type = warrior_type
		self.name = name
		self.weapon = weapon

	def attack(self, attack_type):
		if attack_type == 'light':
			res = self.weapon.light_attack(self)
			return res
		elif attack_type == 'heavy':
			res = self.weapon.heavy_attack(self)
			return res


class Knight(Warrior):
	def __init__(self, name, weapon) -> None:
		super().__init__(name, weapon, "Knight", 100)
		self.light_attack_bonus = 3
		self.heavy_attack_bonus = 3


class Archer(Warrior):
	def __init__(self, name, weapon) -> None:
		super().__init__(name, weapon, "Archer", 110)
		self.light_attack_bonus = 5
		self.heavy_attack_bonus = 1


class Paladin(Warrior):
	def __init__(self, name, weapon) -> None:
		super().__init__(name, weapon, "Knight", 85)
		self.light_attack_bonus = 0
		self.heavy_attack_bonus = 6