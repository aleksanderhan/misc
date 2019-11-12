import sys


ops = {
	'+' : (lambda a, b: a + b),
	'-' : (lambda a, b: a - b),
	'*' : (lambda a, b: a*b),
	'/' : (lambda a, b: a/b) 
}

token_parsers = {
	'in'  : (lambda tkns: (tkns[1], tkns[0:3:2])), # Infix notation a op b
	'pn'  : (lambda tkns: (tkns[0], tkns[1:3])),   # Polish notation, op a b
	'rpn' : (lambda tkns: (tkns[2], tkns[0:2])),   # Reverse polish notation, a b op 
}


# coroutine
def calculator(notation):
	print(f'Starting calculator instance with {notation} notation.')
	while True:
		try:
			tokens = (yield).split(' ')
			op, args = token_parsers[notation](tokens)
			args = map((lambda a: float(a) if ('.' in a) else int(a)), args)
			print(f'= {ops[op](*args)}')
		except Exception as e:
			print(e)

def main(notation):
	calc = calculator(notation)
	next(calc) # Starting coroutine
	while True:
		cmd = str(input(': '))
		if cmd == 'q': break
		calc.send(cmd)


if __name__ == '__main__':
	try:
		notation = sys.argv[1] if (sys.argv[1] in token_parsers.keys()) else 'in'
	except:
		notation = 'in'
	
	main(notation)