from random import randint
import datetime
from Token import Token

def criarToken():
	numero = randint(1111,9999)
	tempo = datetime.datetime.now()
	global token
	token = Token(numero, tempo)
	mostrarToken()

def mostrarToken():
	token.mostrarToken()
	print("\n--------------------\n")
	main()
def apagarToken():
	token = None
def calcularValor():
	saída = datetime.datetime.now()
	diferença = datetime.datetime.now() - token.getTime() #em segundos
	print(f"Voce passou {diferença.seconds} segundos no estacionamento.")
	if(diferença.seconds > 600):
		valor = diferença.seconds * 0.50
		print("O valor do estacionamento é ${:,.2f}".format(valor))
	else:
		print("Não será cobrado taxa de estacionamento!")

def main():
	#Menu principal
	print("\nSeja bem-vind@!")
	if(token == None):
		print("Por favor, anote seu token de estacionamento.")
		criarToken()
	else:
		print("1 - Consulta de Token\n2 - Saindo do estacionamento")
		escolha = int(input("> "))
		if(escolha == 1):
			token.mostrarToken()
			main()
		elif(escolha == 2):
			calcularValor()	
		else:
			print("Opção inválida!\n")
			main()
token = None
saída = 0
main()
