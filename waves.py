import math
import numpy as np

def sine(frequency, length, rate):
	length = int(length * rate)
	factor = float(frequency) * (math.pi * 2) / rate

	return np.sin(np.arange(length) * factor)

def square(frequency, length, rate):
	wave = sine(frequency, length, rate)

	for i in xrange(len(wave)):
		curr = wave[i]
		if curr > 0:
			wave[i] = 0.999
		elif curr < 0:
			wave[i] = -0.999
		else:
			wave[i] = 0

	return wave

def sawtooth(frequency, length, rate):
	length = int(length * rate)
	period = float(rate)/float(frequency)

	wave = np.arange(length)

	for i in xrange(len(wave)):
		wave[i] = i % period

	amax = np.amax(wave)
	amin = np.amin(wave)
	for i in xrange(len(wave)):
		wave[i] = 2*(wave[i]-amin)/(amax-amin)-1

	return wave
