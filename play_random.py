import random
from game.game import Game

if __name__ == "__main__":
	while True:
		game = Game()
		moves = [
			Game.Direction.up,
			Game.Direction.left,
			Game.Direction.down,
			Game.Direction.right
		]
		i = 0
		while True:
			# move = random.choice(moves)
			move = moves[i]
			i = (i + 1) % len(moves)
			game.move(move)

			# print game.state

			if game.over:
				if game.won:
					print 'You Won!'
				else:
					print 'Game Over :( Moves:', game.num_moves, 'Score:', game.score
				break
