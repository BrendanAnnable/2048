from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
import matplotlib.pyplot as plot
import numpy as np
import random
import pybrain as pb
from pybrain.optimization import HillClimber
from game.game import Game

filename = r'C:\Users\1260\Dropbox\lab\2048\network.xml'
nnet = None
errors = []
try:
	nnet = NetworkReader.readFrom(filename)
except IOError:
	nnet = buildNetwork(16, 5, 5, 4)

if True:
	# learn
	def checknn(params):
		#create a network
		nn = buildNetwork(16, 5, 5, 4)

		#assign the parameters to be what we are testing
		i = 0
		for m in nn.connections.values():
			for c in m:
				for j in xrange(len(c.params)):
					c._params[j] = params[i]
					i += 1

		map = {
			0: Game.Direction.left,
			1: Game.Direction.right,
			2: Game.Direction.up,
			3: Game.Direction.down,
		}

		# run here
		game = Game()
		while not game.over:
			if random.random() < 0.95:
				inputs = np.hstack(game.state).tolist()
				outputs = nn.activate(inputs).tolist()
				#print outputs
				m = max(outputs)
				i = outputs.index(m)
				move = map[i]
				#print move
				game.move(move)
			else:
				move = map[random.randint(0, 3)]
				game.move(move)

		error = np.log2(2048 - game.max_block)

		print 'score', game.score
		print 'max block', game.max_block
		print 'error', error
		print

		return error

	hc_params = []
	for m in nnet.connections.values():
		for c in m:
			hc_params.extend(c.params) #extend concatenates 2 arrays

	opt = HillClimber(checknn, hc_params)
	opt.minimize = True
	opt.maxEvaluations = 100000
	opt.learn()

NetworkWriter.writeToFile(nnet, filename)

# r = 15
# xvalues = np.arange(-r, r, 0.1)
# yvalues = [nnet.activate([x]) for x in xvalues]
#
# plot.figure(0)
# plot.plot(xvalues, yvalues)
# xvalues = np.arange(-r, r, 0.1)
# yvalues = [f(x) for x in xvalues]
# plot.plot(xvalues, yvalues)
#
# xvalues = range(len(errors))
# yvalues = errors
# plot.figure(1)
# plot.plot(xvalues, yvalues)
#
# plot.show()

