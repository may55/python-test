import numpy as np


dataset = np.arange(10)

def movingaverage(values,window):
	weights = np.repeat(1.0,window)/window
	print(np.repeat(1.0,window))
	print(weights)
	smas = np.convolve(values,weights,'valid')
	return smas

print(movingaverage(dataset,3))