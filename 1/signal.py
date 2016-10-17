class signal:
	frequency = None
	period = None
	pulsation = None
	def setFrequency(self, frequency):
		self.frequency = frequency
	def setPeriod(self, period):
		self.period = period
	def setPulsation(self, pulsation):
		self.pulsation = pulsation
	def getFrequency(self):
		return self.frequency
	def getPeriod(self):
		return self.period
	def getPulsation(self):
		return self.pulsation