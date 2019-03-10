from parkingManager import *

def mostrarToken(numero): 
	token = tokens[getTokenIndex(numero)]
	print("---- Seu Token ----")
	print(f"Código: {token.getNumero()}")
	print(f"Criado em {token.getTime()}")
	print("\n--------------------\n\n")
	main()

def main():
	print("\nSeja bem-vindo(a)!")
	print("1 - Entrar no estacionamento\n2 - Consultar meu token\n3 - Sair do estacionamento")
	try:
		escolha = int(input("> "))
		if(escolha == 1):
			token = criarToken(input("Placa do veículo (ABC-0000): "))
			if(token==False):
				print("A placa está incorreta!\n")
			else:
				print("Seu token é:", token)
			main()
		elif(escolha == 2):
			mostrarToken(int(input("Digite seu token: ")))
			main()
		elif(escolha == 3):
			token = int(input("Digite seu token: "))
			dados = calcularValor(token)
			print("Você passou",dados["tempo"],"segundos no estacionamento")
			print("O valor do seu estacionamento foi R${:.2f}".format(dados['valor']))
			print("Aguardando o pagamento...")
			system("PAUSE")
			apagarToken(token)
			main()
		else:
			print("Opção inválida!\n")
			main()
	except:
		print("Por favor, digite um número.")
		main()
main()
