from game.game import Game

if __name__ == "__main__":
	game = Game()
	while True:
		print 'Score:', game.score
		print game.state
		m = raw_input('Move (wasd): ')
		if m == 'w':
			game.move(Game.Direction.up)
		elif m == 'a':
			game.move(Game.Direction.left)
		elif m == 's':
			game.move(Game.Direction.down)
		elif m == 'd':
			game.move(Game.Direction.right)

		if game.over:
			if game.won:
				print 'You Won!'
			else:
				print 'Game Over :( Score:', game.score
			break
