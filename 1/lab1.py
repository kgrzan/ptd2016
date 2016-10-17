from signal import *
import matplotlib.pyplot as plt
class lab1:
	data = []
	def printData(self):
		plt.plot(self.data)
		plt.show()
	def setData(self, data):
		for i in data:
			self.data.append(i)
	
	
	