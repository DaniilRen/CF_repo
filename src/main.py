import matplotlib as plt
from game.utils import character_create, move


def game():
	warrior1, warrior2 = character_create()
	cnt = 1
	while warrior1.stamina > 0 and warrior2.stamina > 0:
		if cnt % 2 == 0:
			move(warrior1, warrior2)
		else:
			move(warrior2, warrior1)
		cnt += 1
	if warrior1.stamina <= 0 and warrior1.stamina < warrior2.stamina:
		print(f'{warrior2.name} выиграл!')
	else:
		print(f'{warrior1.name} выиграл!')



print(game())
