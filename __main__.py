import math
import numpy
import pyaudio
from waves import *

def get_wave(frequency=261.6, length=1, rate=44100, type='sine'):
	output = []
	if type=='sine':
		output = numpy.array(sine(frequency, length, rate))
	elif type=='square':
		output = numpy.array(square(frequency, length, rate))
	else:
		output = numpy.array(sawtooth(frequency, length, rate))
	
	return output

def play_tone(output, stream):
	chunks = []

	chunks.append(output)
	
	chunk = numpy.concatenate(chunks) * 0.25

	stream.write(chunk.astype(numpy.float32).tostring())

if __name__ == '__main__':
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paFloat32,
		channels=1, rate=44100, output=1)

	base_freq = 261.6

	output = get_wave(type=sawtooth)
	output = output + get_wave(frequency=base_freq*math.pow(2,4.0/12),type=sawtooth)
	output = output + get_wave(frequency=base_freq*math.pow(2,7.0/12),type=sawtooth)

	play_tone(output, stream)

	stream.close()
	p.terminate()
