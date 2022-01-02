def makebold(fn):
	def wrapper(*s):
		return '<b>'+fn(*s)+'</b>'
	return wrapper
	
def makeitalic(fn):
	def wrapper(*s):
		return '<i>'+fn(*s)+'</i>'
	return wrapper

@makebold
@makeitalic
def htmltag(text):
    return text

print(htmltag('Decorator'))
