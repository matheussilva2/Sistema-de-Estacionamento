import datetime

class Token:
	def __init__(self, numero, time, placa):
		self.__numero = numero
		self.__time = time
		self.__placa = placa

	def getNumero(self):
		return self.__numero

	def getTime(self):
		return self.__time
