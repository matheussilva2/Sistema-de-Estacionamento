from random import randint
import datetime
from Token import Token
from os import system

tarifa = 0.50
tempoDeCobranca = 3 #em segundos
tokens = []

def criarToken(placa):
	numero = randint(1111,9999)
	tempo = datetime.datetime.now()
	tokens.append(Token(numero, tempo, placa))
	return numero

def getTokenIndex(numero):
	posicao = -1
	for index, token in enumerate(tokens):
		if(token.getNumero() == numero):
			posicao = index
			break
	return posicao

def apagarToken(numero):
	tokens.pop(getTokenIndex(numero))


def calcularValor(numero):
	diferenca = datetime.datetime.now() - tokens[getTokenIndex(numero)].getTime() #em segundos
	if(diferenca.seconds > tempoDeCobranca):
		valor = diferenca.seconds * tarifa
		return {'tempo':diferenca.seconds,'valor':valor}
	else:
		return {'tempo':diferenca.seconds,'valor':0}
