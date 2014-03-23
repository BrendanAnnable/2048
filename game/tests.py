from game import Game
import unittest


class Tests(unittest.TestCase):

	def testBasic(self):
		game = Game(4, testing=True)
		game.state = [
			[2, 0, 0, 2],
			[0, 2, 0, 2],
			[0, 0, 2, 2],
			[0, 0, 0, 2]
		]
		game.move(Game.Direction.left)

		self.assertEqual(game.state, [
			[4, 0, 0, 0],
			[4, 0, 0, 0],
			[4, 0, 0, 0],
			[2, 0, 0, 0]
		])

	def testMedium(self):
		game = Game(4, testing=True)
		game.state = [
			[2, 0, 4, 2],
			[0, 2, 0, 2],
			[0, 4, 2, 2],
			[0, 0, 4, 2]
		]
		game.move(Game.Direction.left)

		self.assertEqual(game.state, [
			[2, 4, 2, 0],
			[4, 0, 0, 0],
			[4, 4, 0, 0],
			[4, 2, 0, 0]
		])

	def testHarder(self):
		game = Game(4, testing=True)
		game.state = [
			[2, 0, 4, 2],
			[0, 2, 0, 2],
			[0, 4, 2, 2],
			[0, 0, 4, 2]
		]

		game.move(Game.Direction.left)
		self.assertEqual(game.state, [
			[2, 4, 2, 0],
			[4, 0, 0, 0],
			[4, 4, 0, 0],
			[4, 2, 0, 0]
		])

		game.move(Game.Direction.up)
		self.assertEqual(game.state, [
			[2, 8, 2, 0],
			[8, 2, 0, 0],
			[4, 0, 0, 0],
			[0, 0, 0, 0]
		])

		game.move(Game.Direction.right)
		self.assertEqual(game.state, [
			[0, 2, 8, 2],
			[0, 0, 8, 2],
			[0, 0, 0, 4],
			[0, 0, 0, 0]
		])

		game.move(Game.Direction.down)
		self.assertEqual(game.state, [
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 4],
			[0, 2, 16, 4]
		])

	def testHarderer(self):
		game = Game(4, testing=True)
		game.state = [
			[4, 0, 4, 4],
			[2, 0, 2, 2],
			[4, 4, 0, 2],
			[2, 0, 2, 4]
		]

		game.move(Game.Direction.right)
		self.assertEqual(game.state, [
			[0, 0, 4, 8],
			[0, 0, 2, 4],
			[0, 0, 8, 2],
			[0, 0, 4, 4]
		])

	def testGameOver(self):
		game = Game(4, testing=True)
		game.state = [
			[4, 0, 4, 4],
			[2, 0, 2, 2],
			[4, 4, 0, 2],
			[2, 0, 2, 4]
		]
		self.assertEqual(game.is_moves_available(), True)

		game.state = [
			[4, 2, 4, 2],
			[2, 4, 2, 4],
			[4, 2, 4, 2],
			[2, 4, 2, 4]
		]
		self.assertEqual(game.is_moves_available(), False)

		game.state = [
			[4, 2, 4, 2],
			[2, 4, 2, 4],
			[4, 2, 4, 2],
			[2, 4, 0, 8]
		]
		self.assertEqual(game.is_moves_available(), True)

		game.state = [
			[ 4,  2,  8,  2],
			[ 2,  4, 16,  2],
			[32, 16, 64,  8],
			[ 4,  2,  4,  2]
		]
		self.assertEqual(game.is_moves_available(), True)


if __name__ == '__main__':
	# begin test

	unittest.main()

