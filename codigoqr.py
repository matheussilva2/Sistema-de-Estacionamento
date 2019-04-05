import qrcode

def gerarCodigo(texto):
	txt = str(texto)
	qrcode.make(txt).save('./'+txt+'.png')
