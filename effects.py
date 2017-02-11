import math
import numpy as np

# inp = input wave as array of values
# degree = fraction of max amplitude of wave to clip
def clip(inp, degree=0.4):
	if (degree <= 0 or degree >= 1):
		degree = 0.4
	amax = np.amax(inp)
	new_max = amax*(1.0-degree)

	for i in xrange(len(inp)):
		if (inp[i] > new_max):
			inp[i] = new_max
		elif (abs(inp[i]) > new_max):
			inp[i] = new_max*-1

	return inp
