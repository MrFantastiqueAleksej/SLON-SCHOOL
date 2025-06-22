def func(num1, num2, clb):
	res = clb(num1) + num2
	return res
	
multpl = lambda numr: numr ** 3
	
print(func(2, 6, multpl))