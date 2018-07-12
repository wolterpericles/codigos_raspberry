"""
Plotar dados das portas do atmega328
"""

import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque

import matplotlib.pyplot as plt 
import matplotlib.animation as animation

    
# classe para portas analogicas 
class AnalogPlot:
  	
	def __init__(self, strPort, maxLen):
		# abrir porta serial
		self.ser = serial.Serial(strPort, 9600)

		self.ax = deque([0.0]*maxLen)
		self.ay = deque([0.0]*maxLen)
		self.maxLen = maxLen

  	# adicionar buffer
	def addToBuf(self, buf, val):
		if len(buf) < self.maxLen:
			buf.append(val)
		else:
			buf.pop()
			buf.appendleft(val)

  	# adicionar dados
	def add(self, data):
		assert(len(data) == 2)
		self.addToBuf(self.ax, data[0])
		self.addToBuf(self.ay, data[1])

  	# atualizar plotagem
	def update(self, frameNum, a0, a1):
		try:
			line = self.ser.readline()
			data = [float(val) for val in line.split()]
			# print data
			if(len(data) == 2):
				self.add(data)
				a0.set_data(range(self.maxLen), self.ax)
				a1.set_data(range(self.maxLen), self.ay)
		except KeyboardInterrupt:
			print('exiting')
	
		return a0, 

  	# sair
	def close(self):
		# sair da serial
		self.ser.flush()
		self.ser.close()    

# funcao principal
def main():
  	# criar parser
  	parser = argparse.ArgumentParser(description="Plotar serial")
  	# adicionar expected arguments
  	parser.add_argument('--porta', dest='port', required=True)

  	# parse args
  	args = parser.parse_args()
  
  	#strPort = '/dev/ttyS0' 
  	strPort = args.port

  	print('Lendo a porta serial %s...' % strPort)

  	# plotando parametros
  	analogPlot = AnalogPlot(strPort, 100)

  	print('plotando dados...')

  	# animacao
  	fig = plt.figure()
  	ax = plt.axes(xlim=(0, 100), ylim=(0, 1023))
  	a0, = ax.plot([], [])
  	a1, = ax.plot([], [])
  	anim = animation.FuncAnimation(fig, analogPlot.update, 
                                 fargs=(a0, a1), 
                                 interval=50)

  	# mostrar plotagem
  	plt.title('Plotar Serial')
  	plt.show()
  
  	# sair
  	analogPlot.close()

  	print('exiting.')
  

# main
if __name__ == '__main__':
	main()