from random import randint
import datetime
from Token import Token
from os import system

tarifa = 0.50
tempoDeCobranca = 3 #em segundos
tokens = []
def validarPlaca(placa):
	if(placa[0:3].isalpha() and placa[4:].isdigit()):
		return True
	else:
		return False

def criarToken(placa):
	if(validarPlaca(placa)):
		numero = randint(1111,9999)
		tempo = datetime.datetime.now()
		adicionarToken(Token(numero, tempo, placa))
		return numero
	else:
		return False

def getTokenIndex(numero):
	for index, token in enumerate(tokens):
		if(token.getNumero() == numero):
			return index
			break

def adicionarToken(token):
	tokens.append(token)

def apagarToken(numero):
	tokens.pop(getTokenIndex(numero))


def calcularValor(numero):
	tempoEstacionado = datetime.datetime.now() - tokens[getTokenIndex(numero)].getTime() #em segundos
	if(tempoEstacionado.seconds > tempoDeCobranca):
		valor = tempoEstacionado.seconds * tarifa
		return {'tempo':tempoEstacionado.seconds,'valor':valor}
	else:
		return {'tempo':tempoEstacionado.seconds,'valor':0}
