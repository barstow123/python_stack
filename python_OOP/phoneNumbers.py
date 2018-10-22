phone = {'0': 'O', '1': 'I', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}

def teleNum(number):
	if len(number) == 1:
		lista = [c for c in phone[number]]
		print('lista:', lista)
		return lista
	else:
		a = teleNum(number[0])
		sols= []
		for i in a:
			r = teleNum(number[1:])
			print('i:', i, 'a:', a, 'r:', r)
			sols.extend([i + rr for rr in r])
			print('sols:', sols)
		return sols

a = sorted(teleNum('8182612'))
print(a)
print(len(a))