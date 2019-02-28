from random import randint
import datetime
from Token import Token

tokens = []

def criarToken():
	numero = randint(1111,9999)
	tempo = datetime.datetime.now()
	tokens.append(Token(numero, tempo))
	return numero

def getTokenIndex(numero):
	posicao = 0
	for index, token in enumerate(tokens):
		if(token.getNumero() == numero):
			posicao = index
			break
	return posicao

def apagarToken(numero):
	tokens.pop(getTokenIndex(numero))

def calcularValor():
	diferença = datetime.datetime.now() - token.getTime() #em segundos
	if(diferença.seconds > 600):
		valor = diferença.seconds * 0.50
		return valor
	else:
		return 0