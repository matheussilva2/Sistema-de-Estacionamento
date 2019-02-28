from parkingManager import *

def mostrarToken(numero): 
	tokens[getTokenIndex(numero)].mostrarToken()
	print("\n--------------------\n\n")
	main()


def main():
	print("\nSeja bem-vind@!")
	print("1 - Criar Token\n2 - Consulta de Token\n3 - Saindo do estacionamento")
	escolha = int(input("> "))
	if(escolha == 1):
		print("Seu token é:", criarToken())
		main()
	elif(escolha == 2):
		mostrarToken(int(input("Numero: ")))
		main()
	elif(escolha == 3):
		calcularValor()	
	else:
		print("Opção inválida!\n")
		main()
main()
