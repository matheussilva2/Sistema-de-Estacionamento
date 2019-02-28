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
	escolha = int(input("> "))
	if(escolha == 1):
		print("Seu token é:", criarToken(input("Placa do veículo: ")))
		main()
	elif(escolha == 2):
		mostrarToken(int(input("Digite seu token: ")))
		main()
	elif(escolha == 3):
		token = input("Digite seu token: ")
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
main()
