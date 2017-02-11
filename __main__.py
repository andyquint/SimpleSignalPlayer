import math
import numpy
import pyaudio
from waves import *

def play_tone(stream, frequency=261.6, length=1, rate=44100):
	chunks = []
	output1 = numpy.array(sawtooth(frequency, length, rate))
	output2 = numpy.array(sawtooth(frequency*5, length, rate))
	combined = output1 + output2

	chunks.append(combined)
	
	chunk = numpy.concatenate(chunks) * 0.25

	stream.write(chunk.astype(numpy.float32).tostring())

if __name__ == '__main__':
	p = pyaudio.PyAudio()
	stream = p.open(format=pyaudio.paFloat32,
		channels=1, rate=44100, output=1)

	play_tone(stream)

	stream.close()
	p.terminate()
