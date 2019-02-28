import datetime

class Token:
	def __init__(self, numero, time):
		self.__numero = numero
		self.__time = time
		self.__válido = False
		self.validarToken()

	def getNumero(self):
		return self.__numero

	def getTime(self):
		return self.__time
		
	def isValid(self):
		return self.__válido

	def usarToken(self):
		self.__válido = False
	def validarToken(self):
		self.__válido = True
	def mostrarToken(self):
		print("---- Seu Token ----")
		print(f"Código: {self.getNumero()}")
		print(f"Criado em {self.getTime()}")
		if(self.isValid):
			print("Este token está válido!")
		else:
			print("Este token é inválido!")